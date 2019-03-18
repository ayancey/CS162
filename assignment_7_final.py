# Dead simple roguelike
# Alex Yancey
# Joseph Jess, CS162

# i tried to implement this myself but math is hard :(
from bresenham import bresenham
import curses
import math
import random
import getpass
import time


class Tile(object):
    def __init__(self, blocking, block_sight, c):
        self.blocking = blocking
        self.block_sight = block_sight
        self.c = c


# Initialize curses
stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)


# all intents
INTENT_MOVE_UP = 0
INTENT_MOVE_DOWN = 1
INTENT_MOVE_LEFT = 2
INTENT_MOVE_RIGHT = 3
INTENT_ATTACK = 4
INTENT_FIRE = 5
INTENT_RELOAD = 6


all_messages = []


def status(msg):
    global all_messages
    all_messages.append(msg)


class Object(object):
    name = None
    attack_verb = None

    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

        self.intent = None

    def draw(self):
        stdscr.addstr(self.y + 1, self.x, self.c)

    def ai(self, p):
        pass


class Killable(Object):
    pass


class Enemy(Killable):
    # TODO: Make this less shitty
    # Pass player object, for tracking
    def ai(self, p):
        # Decide to move up/down/left/right, based on where the player is

        # Move vertically or horizontally based on a coin flip, makes the movement look more realistic
        vert_or_horiz = random.choice([True, False])

        needed_intent = None
        if p.y < self.y:
            needed_intent = INTENT_MOVE_UP
        elif p.y > self.y:
            needed_intent = INTENT_MOVE_DOWN

        if needed_intent is not None:
            if vert_or_horiz:
                self.intent = needed_intent
                return

        if p.x < self.x:
            self.intent = INTENT_MOVE_LEFT
        elif p.x > self.x:
            self.intent = INTENT_MOVE_RIGHT


class Player(Killable):
    # set player name to username of computer
    name = getpass.getuser()
    attack_dmg = 2
    attack_verb = "{} defends helplessly against the {}"
    bullet_dmg = 7
    bullet_rounds = 8


class Zombie(Enemy):
    name = "Zombie"
    attack_dmg = 3
    attack_verb = "{} claws at {}"

    # Make zombies red
    def draw(self):
        stdscr.addstr(self.y + 1, self.x, self.c, curses.color_pair(2))


player = Player(2, 2, "@")
player.hp = 10

all_objects = [player]

tiles = []

width = 100
height = 20

# Create all blank tiles to start with
for i in range(height):
    new = []
    for j in range(width):
        new.append(Tile(False, False, "."))
    tiles.append(new)


def vert_wall(x, y, h):
    for i in range(h):
        tiles[i + y][x] = Tile(True, True, "#")


def horiz_wall(x, y, w):
    for i in range(w):
        tiles[y][x + i] = Tile(True, True, "#")


# box in everything
horiz_wall(0, 0, width)
horiz_wall(0, height - 1, width)
vert_wall(0, 0, height)
vert_wall(width - 1, 0, height)


# maze like

vert_wall(5, 0, 5)
horiz_wall(0, 7, 10)

vert_wall(20, 0, 10)
horiz_wall(0, 12, 30)

vert_wall(25, 0, 10)

vert_wall(29, 12, 8)
vert_wall(33, 12, 8)

vert_wall(40, 0, height)


# sort of expensive method, use wisely
def has_los(a, b):
    bres = list(bresenham(a.x, a.y, b.x, b.y))
    # a can't block itself
    bres.remove((a.x, a.y))

    for point in bres:
        if tiles[point[1]][point[0]].block_sight:
            return False

    return True


# Spawn a bunch of zombies, out of line of sight to the player, and on the map somewhere
for i in range(30):
    while True:
        x = random.randint(1, width - 1)
        y = random.randint(1, height - 1)
        if tiles[y][x].c == ".":
            another_object_occupying = False

            for o in all_objects:
                if o.x == x:
                    if o.y == y:
                        another_object_occupying = True

            if not another_object_occupying:
                z = Zombie(x, y, "z")
                z.hp = 10
                if not has_los(player, z):
                    all_objects.append(z)
                    break


def draw_everything():
    # global variables are bad, sorry
    global stdscr
    global all_messages

    stdscr.erase()

    # Draw tiles, if they're not blocked by a tile that blocks sight
    for y, row in enumerate(tiles):
        for x, column in enumerate(row):
            do_draw = True

            b = list(bresenham(player.x, player.y, x, y))

            # object can't block itself
            b.remove((x, y))

            for point in b:
                if tiles[point[1]][point[0]].block_sight:
                    do_draw = False
                    break

            if do_draw:
                stdscr.addstr(y + 1, x, column.c, curses.color_pair(1))
            else:
                stdscr.addstr(y + 1, x, " ")

    # Cheap hack to make the player always stand on top of objects
    if player.hp > 0:
        all_objects.remove(player)
        all_objects.append(player)

    # Draw objects, if they're not blocked by a tile that blocks sight
    for o in all_objects:
        b = list(bresenham(player.x, player.y, o.x, o.y))

        do_draw = True

        for point in b:
            if tiles[point[1]][point[0]].block_sight:
                do_draw = False
                break

        if do_draw:
            o.draw()

    # Show status messages, which disappear after next turn
    if all_messages:
        prepared = ""

        # Quick hack to make duplicate messages be displayed more elegantly
        message_frequency = {}
        for msg in all_messages:
            if msg in message_frequency:
                message_frequency[msg] += 1
            else:
                message_frequency[msg] = 1
        all_messages = []
        for msg in message_frequency:
            if message_frequency[msg] > 1:
                all_messages.append("{} x{}".format(msg, message_frequency[msg]))
            else:
                all_messages.append(msg)

        for n, msg in enumerate(all_messages):
            prepared += msg
            if n < len(all_messages) - 1:
                prepared += ", "
        stdscr.addstr(0, 0, prepared)
        all_messages = []

    stdscr.refresh()


if __name__ == "__main__":
    status("Welcome to my final project! f: fire, r: reload, q: quit")

    reload_delay = False

    # The main game loop.
    while True:
        if reload_delay:
            reload_delay = False
            # one last hack
            status("{} finishes reloading".format(getpass.getuser()))
        for o in all_objects:
            # Allow objects to make decisions, leading to intents
            o.ai(player)

            theoretical_x = o.x
            theoretical_y = o.y

            # Handle intents
            if o.intent == INTENT_MOVE_UP:
                theoretical_y -= 1
            elif o.intent == INTENT_MOVE_DOWN:
                theoretical_y += 1
            elif o.intent == INTENT_MOVE_LEFT:
                theoretical_x -= 1
            elif o.intent == INTENT_MOVE_RIGHT:
                theoretical_x += 1

            # Move the object if it's not being blocked
            if not tiles[theoretical_y][theoretical_x].blocking:
                target = None

                # If a killable object is about to move into another killable object, set its intent to attack
                if isinstance(o, Killable):
                    for oo in all_objects:
                        if theoretical_x == oo.x:
                            if theoretical_y == oo.y:
                                if o != oo:
                                    # Zombies won't attack other zombies
                                    if type(o) != type(oo):
                                        if isinstance(oo, Killable):
                                            # only announce things if the player can see it
                                            if o == player or has_los(player, o):
                                                status(o.attack_verb.format(o.name, oo.name))
                                            target = oo
                                            o.intent = INTENT_ATTACK
                                        else:
                                            if o == player or has_los(player, o):
                                                status("{} stands on a {}".format(o.name, oo.name))

                if not o.intent == INTENT_ATTACK:
                    # When moving, you can step on objects, but you can't step on other players/enemies
                    no_objects_intheway = True
                    for oo in all_objects:
                        if theoretical_x == oo.x:
                            if theoretical_y == oo.y:
                                if isinstance(oo, Killable):
                                    no_objects_intheway = False

                    if no_objects_intheway:
                        o.x = theoretical_x
                        o.y = theoretical_y

                if o.intent == INTENT_ATTACK:
                    # Attacker can do between 50% and 150% of their base damage
                    projected_dmg = int(o.attack_dmg * (random.randint(5, 15) / 10))

                    target.hp -= projected_dmg

                    if target.hp < 1:
                        if o == player or has_los(player, o):
                            status("{} has died!".format(target.name))
                        corpse = Object(target.x, target.y, "c")
                        corpse.name = "{} corpse".format(target.name)
                        corpse.hp = 100
                        all_objects.remove(target)
                        all_objects.append(corpse)

            if o.intent == INTENT_FIRE:
                closest_killable_object = None
                lowest_dist = None

                for oo in all_objects:
                    if o != oo:
                        if isinstance(oo, Killable):
                            if has_los(o, oo):
                                dist = math.sqrt(((oo.x - o.x)**2) + ((oo.y - o.y)**2))
                                if lowest_dist is None:
                                    lowest_dist = dist
                                    closest_killable_object = oo
                                else:
                                    if dist < lowest_dist:
                                        lowest_dist = dist
                                        closest_killable_object = oo

                # Unfortunately, I found myself repeating a lot of logic from the attack intent. It would be nice to refactor this.
                if closest_killable_object:
                    accuracy = 100 - ((lowest_dist ** 0.7) * 10)
                    status("{} takes aim at {}".format(o.name, closest_killable_object.name))

                    if o.bullet_rounds < 1:
                        status("You must reload!")
                    else:
                        if random.randint(1, 100) < accuracy:
                            status("{} hits the {}".format(o.name, closest_killable_object.name))
                            potential_dmg = o.bullet_dmg * (accuracy / 100)
                            closest_killable_object.hp -= potential_dmg
                            if closest_killable_object.hp < 1:
                                # TODO: Stop repeating logic from attack intent
                                if closest_killable_object == player or has_los(player, closest_killable_object):
                                    status("{} has died!".format(closest_killable_object.name))
                                corpse = Object(closest_killable_object.x, closest_killable_object.y, "c")
                                corpse.name = "{} corpse".format(closest_killable_object.name)
                                corpse.hp = 100
                                all_objects.remove(closest_killable_object)
                                all_objects.append(corpse)
                        else:
                            status("{} misses the {}".format(o.name, closest_killable_object.name))

                        casing = Object(o.x, o.y, "=")
                        casing.name = "shell casing"
                        all_objects.append(casing)

                        o.bullet_rounds -= 1
                else:
                    if o == player:
                        status("{} doesn't see anything to shoot".format(o.name))

            if o.intent == INTENT_RELOAD:
                status("{} starts reloading".format(o.name))
                clip = Object(o.x, o.y, "/")
                clip.name = "empty clip"
                all_objects.append(clip)
                o.bullet_rounds = 8
                # cheap hack to make the game progress one extra turn before the player can do anything
                reload_delay = True

            # Always reset their intent to nothing, this allows the next turn to continue
            o.intent = None

        # Draw tiles, and objects
        draw_everything()

        # One last indicator the player is dead
        if player.hp < 1:
            stdscr.addstr(0, 0, "You died!", curses.A_REVERSE)

        if reload_delay:
            time.sleep(1)
        else:
            # Ask the user what their next move is
            key = stdscr.getkey()

            if key == "KEY_UP":
                player.intent = INTENT_MOVE_UP
            elif key == "KEY_DOWN":
                player.intent = INTENT_MOVE_DOWN
            elif key == "KEY_LEFT":
                player.intent = INTENT_MOVE_LEFT
            elif key == "KEY_RIGHT":
                player.intent = INTENT_MOVE_RIGHT
            elif key == "f":
                player.intent = INTENT_FIRE
            elif key == "r":
                player.intent = INTENT_RELOAD
            elif key == "q":
                break

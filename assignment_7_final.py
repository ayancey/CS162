# Dead simple roguelike
# Loosely following libtcod tutorial on roguebasin.com
# Alex Yancey
# Joseph Jess, CS162

import random
import curses
import math

# i tried to implement this myself but math is hard :(
from bresenham import bresenham


class Tile(object):
    def __init__(self, blocking, block_sight, c):
        self.blocking = blocking
        self.block_sight = block_sight
        self.c = c



# Initialize curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


# all intents
INTENT_MOVE_UP = 0
INTENT_MOVE_DOWN = 1
INTENT_MOVE_LEFT = 2
INTENT_MOVE_RIGHT = 3


class Object(object):
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

        self.intent = None

    def draw(self):
        stdscr.addstr(self.y + 1, self.x, self.c)

    def ai(self):
        pass


class Enemy(Object):
    def ai(self):
        pass
        #self.intent = INTENT_MOVE_UP


player = Object(2, 2, "@")
monster = Enemy(5, 10, "s")


all_objects = [player, monster]

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


def draw_stuff_2():
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
                stdscr.addstr(y + 1, x, column.c)
            else:
                stdscr.addstr(y + 1, x, " ")

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


while True:
    stdscr.addstr(0,0, "Nice")

    for o in all_objects:
        # Allow objects to make decisions, leading to intents
        o.ai()

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
            o.x = theoretical_x
            o.y = theoretical_y

        o.intent = None


    # Draw everything
    draw_stuff_2()

    #stdscr.refresh()

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

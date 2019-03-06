# Dead simple roguelike
# Alex Yancey
# Joseph Jess, CS162
import random
import curses
import math

# i tried to implement this myself but math is hard :(
from bresenham import bresenham


tiles = []

width = 100
height = 20

for i in range(height):
    l = []
    for j in range(width):
        l.append(".")
    tiles.append(l)


def room(start_x, start_y, width, height):
    for y in range(width):
        for x in range(height):
            tiles[start_y + y][start_x + x] = "#"

    for y in range(width - 2):
        for x in range(height - 2):
            tiles[start_y + y + 1][start_x + x + 1] = "."

    #tiles[start_y + 2][start_x + 4] = "@"



# reference is top left of room


player_y = height // 2
player_x = width // 2


money_y = player_y - 5
money_x = player_x - 15

dist_x = money_x - player_x
dist_y = money_y - player_y



# money
tiles[money_y][money_x] = "$"

#wall
for i in range(10):
    tiles[(player_y - 5) + i][player_x - 10] = "#"

# player




# for point in bresenham(player_x, player_y, money_x, money_y):
#     tiles[point[1]][point[0]] = "#"
#     print(point)

#
# while True:
#     if target_x < money_x:
#         target_x += 1
#     elif target_x > money_x:
#         target_x -= 1
#
#     if target_y < money_y:
#         target_y += 1
#     elif target_y > money_y:
#         target_y -= 1
#
#     tiles[target_y][target_x] = "#"
#
#     if target_x == money_x:
#         if target_y == money_y:
#             break


# print((target_x, target_y))
# print((money_x, money_y))


# # up
# for i in range(5):
#     tiles[player_y - 1 -  i][player_x] = "|"
#
# # down
# for i in range(5):
#     tiles[player_y + i + 1][player_x] = "|"
#
# # left
# for i in range(5):
#     tiles[player_y][player_x -i - 1] = "-"
#
# # right
# for i in range(5):
#     tiles[player_y][player_x + i + 1] = "-"
#
# # up left
# for i in range(5):
#     tiles[player_y -1 - i][player_x -i - 1] = "-"
#
# # up right
# for i in range(5):
#     tiles[player_y -1 - i][player_x +i + 1] = "-"
#
#
# # bottom left
# for i in range(5):
#     tiles[player_y +1 +i][player_x -i - 1] = "-"
#
# # bottom right
# for i in range(5):
#     tiles[player_y +1 + i][player_x +i + 1] = "-"


#
# room(start_x, start_y, 5, 5)
#
# room(0, 0, 5, 5)

#input()


class Object(object):
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

    def draw(self):
        stdscr.addstr(self.y, self.x, c)


class Tile(object):
    def __init__(self):
        pass


#representation = ""


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


def draw_stuff():
    for y, row in enumerate(tiles):
        for x, column in enumerate(row):
            blocked = False
       # if column == "$":
            if column != "#":
                b = list(bresenham(player_x, player_y, x, y))
                if len(b) < 5:
                    for point in b:
                        #print(point)
                        if tiles[point[1]][point[0]] == "#":
                            blocked = True
                else:
                    blocked = True


            if blocked:
                stdscr.addstr(y, x, " ")
            else:
                stdscr.addstr(y, x, column)
        # representation += "\n"

while True:
    key = stdscr.getkey()

    if key == "KEY_UP":
        player_y -= 1
    elif key == "KEY_DOWN":
        player_y += 1
    elif key == "KEY_LEFT":
        player_x -= 1
    elif key == "KEY_RIGHT":
        player_x += 1

    draw_stuff()
    stdscr.addstr(player_y, player_x, "@")
    stdscr.refresh()


#
# tiles[room_start] = "."
#
# representation = ""
#
# for n, t in enumerate(tiles):
#     if (n % width) == 0:
#         representation += "\n"
#     representation += t
#
# print(representation)

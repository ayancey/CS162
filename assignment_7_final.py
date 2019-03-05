# Dead simple roguelike
# Alex Yancey
# Joseph Jess, CS162
import random
import curses

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


money_y = player_y
money_x = player_x - 15

dist_x = money_x - player_x
dist_y = money_y - player_y

print(dist_y, dist_x)

# money
tiles[money_y][money_x] = "$"

# wall
for i in range(10):
    tiles[(player_y - 5) + i][player_x - 10] = "#"

# player
tiles[player_y][player_x] = "@"

# up
for i in range(5):
    tiles[player_y - 1 -  i][player_x] = "|"

# down
for i in range(5):
    tiles[player_y + i + 1][player_x] = "|"

# left
for i in range(5):
    tiles[player_y][player_x -i - 1] = "-"

# right
for i in range(5):
    tiles[player_y][player_x + i + 1] = "-"

# up left
for i in range(5):
    tiles[player_y -1 - i][player_x -i - 1] = "-"

# up right
for i in range(5):
    tiles[player_y -1 - i][player_x +i + 1] = "-"


# bottom left
for i in range(5):
    tiles[player_y +1 +i][player_x -i - 1] = "-"

# bottom right
for i in range(5):
    tiles[player_y +1 + i][player_x +i + 1] = "-"


#
# room(start_x, start_y, 5, 5)
#
# room(0, 0, 5, 5)

#input()



representation = ""

for y, row in enumerate(tiles):
    for x, column in enumerate(row):
        #dist_x =


        #print((x, y))
        # visible
        representation += column
    representation += "\n"

print(representation)

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

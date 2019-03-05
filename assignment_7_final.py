

tiles = []

width = 100
height = 20

for i in range(height):
    l = []
    for j in range(width):
        l.append("#")
    tiles.append(l)


room_start_y = height // 2
room_start_x = width // 2





representation = ""

for row in tiles:
    for column in row:
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

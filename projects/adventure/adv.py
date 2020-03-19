from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


the_rooms = {}

for room in world.rooms:
    the_rooms[room] = set()
    for direction in world.rooms[room].get_exits():
        the_rooms[room].add(direction)


def connections(room):
    return the_rooms[room]


def dft(starting_location):
    s = Stack()

    s.push(starting_location)

    visited = set()

    while s.size() > 0:

        v = s.pop()

        if v.id not in visited:
            visited.add(v.id)
            for direction in connections(v.id):
                if direction == 'n':
                    s.push(v.n_to)
                elif direction == 's':
                    s.push(v.s_to)
                elif direction == 'e':
                    s.push(v.e_to)
                else:
                    s.push(v.w_to)

    return visited


# print(player.current_room.id)
print(dft(player.current_room))
print(traversal_path)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

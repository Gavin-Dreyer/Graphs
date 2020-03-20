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

# Create connections for the rooms
# ex: {0: {('n', 1)}, 1: {('n', 2), ('s', 0)}, 2: {('s', 1)}}
the_rooms = {}

for room in world.rooms:
    the_rooms[room] = set()
    for direction in world.rooms[room].get_exits():
        if direction == 'n':
            direction = ('n', world.rooms[room].n_to.id)
            the_rooms[room].add(direction)
        elif direction == 's':
            direction = ('s', world.rooms[room].s_to.id)
            the_rooms[room].add(direction)
        elif direction == 'e':
            direction = ('e', world.rooms[room].e_to.id)
            the_rooms[room].add(direction)
        elif direction == 'w':
            direction = ('w', world.rooms[room].w_to.id)
            the_rooms[room].add(direction)


def connections(room):
    """
    room connections
    """
    return the_rooms[room]


# number of moves counter
counter = 0

# starts in dft and progresses with player_traversal


def player_traversal(current_location, next_location):
    # no move to be made
    if current_location.id == next_location.id:
        return
    else:
        # Use a breadth first search to find the shortest path between room that need to be navigated through
        # ex:
        # 0 3
        # 3 4
        # 4 7
        # 7 8
        # 8 1
        # 1 2
        # 2 5
        # 5 6

        q = Queue()

        q.enqueue([(current_location, current_location.id)])

        path = []
        visited_bfs = set()

        while q.size() > 0:
            v = q.dequeue()

            vert = v[-1]
            if vert[1] not in visited_bfs:
                visited_bfs.add(vert[1])
                if vert[1] == next_location.id:
                    global counter
                    # move the player based on the path provided by the BFS
                    # ex: of navigation the cross map from room 8 to room 1
                    # (<room.Room object at 0x10b7ae1d0>, 8), ('e', 7), ('e', 0), ('n', 1)]
                    for i in range(1, len(v)):
                        counter += 1
                        player.travel(v[i][0])
                        visited_rooms.add(player.current_room)
                else:
                    # standard queue structure
                    for i in connections(vert[1]):
                        if i[0] == 'n':
                            temp = v.copy()
                            temp.append(i)
                            q.enqueue(temp)
                        elif i[0] == 's':
                            temp = v.copy()
                            temp.append(i)
                            q.enqueue(temp)
                        elif i[0] == 'e':
                            temp = v.copy()
                            temp.append(i)
                            q.enqueue(temp)
                        elif i[0] == 'w':
                            temp = v.copy()
                            temp.append(i)
                            q.enqueue(temp)

# Use a depth first traversal to navigate through every path


def dft(starting_location):
    s = Stack()

    s.push(starting_location)

    visited = set()

    while s.size() > 0:
        # v is for vertex(room)
        v = s.pop()

        if v.id not in visited:
            current = starting_location

            # pass in the starting location and the next room for player_traversal, also only pass in rooms that need to be traversed through
            player_traversal(current, v)

            # update current to next room for next loop
            current.id = v.id

            visited.add(v.id)
            # add adjacent rooms to the stack from which ever is the most recently popped room
            for direction in connections(v.id):
                if direction[0] == 'n':
                    s.push(v.n_to)
                elif direction[0] == 's':
                    s.push(v.s_to)
                elif direction[0] == 'e':
                    s.push(v.e_to)
                else:
                    s.push(v.w_to)
    return visited


print(dft(player.current_room))
print(counter)
# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

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

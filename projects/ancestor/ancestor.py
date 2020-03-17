from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):

    def neighbors(ancestors):
        """
        Build the graph
        """
        individual_ancestors = {}
        for ancestor in ancestors:
            # create a new set for each ancestor, ancestors come in pairs of two. [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
            #      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
            for i in range(len(ancestor)):
                if ancestor[i] not in individual_ancestors:
                    individual_ancestors[ancestor[i]] = set()

        # assign each child to it ancestor because we are searching from the bottom up to find the oldest ancestor
        for ancestor in ancestors:
            individual_ancestors[ancestor[1]].add(ancestor[0])
        return individual_ancestors

    def get_neighbors(vert):
        # find existing connections for the child to its ancestor
        connections = neighbors(ancestors)
        if vert in connections:
            return connections[vert]

    # create a stack because we are using a depth first search
    s = Stack()

    s.push([starting_node])

    visited = set()
    path = []
    while s.size() > 0:

        v = s.pop()

        vert = v[-1]

        if vert not in visited:
            path.append(vert)
            visited.add(vert)

            for neighbor in get_neighbors(vert):
                path_copy = path.copy()
                path_copy.append(neighbor)
                s.push(path_copy)

    # if the starting node has no ancestors, return -1
    if len(path) == 1:
        return -1
    else:
        # using the created path we need to return the last element in the array, but if their are two equal ancestors to a child, return the numerically smallest one
        earliest = []
        # if there is no ancestors to an item, it is one of the earliest ancestors
        for p in path:
            if len(get_neighbors(p)) == 0:
                earliest.append(p)

        # if there is only one earliest ancestor, return that one
        if len(earliest) == 1:
            return earliest[0]
        else:
            # if there is more than one compare it to the path to check for the earliest of the earliest ancestors
            for i in range(len(earliest) - 1):
                # if the ancestors in the earliest array are seperated by more than 1 index, they are on different levels of the tree. If they are within one index of each other, they are on the same level of the tree, so return the numerically smallest of the two.
                if path.index(earliest[i + 1]) - path.index(earliest[i]) < 2:
                    return min(earliest)
                else:
                    return earliest[-1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 1))
# print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 3))
# print(earliest_ancestor(test_ancestors, 4))
# print(earliest_ancestor(test_ancestors, 5))
print(earliest_ancestor(test_ancestors, 6))
# print(earliest_ancestor(test_ancestors, 7))
print(earliest_ancestor(test_ancestors, 8))
print(earliest_ancestor(test_ancestors, 9))
# print(earliest_ancestor(test_ancestors, 10))
# print(earliest_ancestor(test_ancestors, 11))

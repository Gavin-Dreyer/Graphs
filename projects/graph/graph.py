"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR: Vertext does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("ERROR: Vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all of its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

        q = []
        visited = {1, 2, 4, 3, 6, 7, 5}

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:

            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all of its neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if the node has been visited
            # If not...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Call dft_recursive on each neighbor
                if self.get_neighbors(v):
                    for i in self.get_neighbors(v):
                        s.push(i)
                        self.dft_recursive(i)
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue A PATH TO starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            vert = v[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if vert not in visited:
                # Mark it as visited
                print(vert)
                visited.add(vert)
                # CHECK IF ITS THE TARGET
                if vert == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return v
                else:
                    # Enqueue A PATH TO ALL of its neighbors
                    for i in self.get_neighbors(vert):
                        # MAKE A COPY OF THE PATH
                        temp = v.copy()
                        temp.append(i)
                        # ENQUEUE THE COPY
                        q.enqueue(temp)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            vert = v[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if vert not in visited:
                # Mark it as visited
                visited.add(vert)
                # CHECK IF ITS THE TARGET
                if vert == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return v
                else:
                    # Push A PATH TO ALL of its neighbors
                    for i in self.get_neighbors(vert):
                        # MAKE A COPY OF THE PATH
                        temp = v.copy()
                        temp.append(i)
                        # PUSH THE COPY
                        s.push(temp)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        s = Stack()

        # Push the starting vertex
        s.push(starting_vertex)
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            if isinstance(v, list):
                vert = v[-1]
            else:
                vert = v
            # Check if the node has been visited
            # If not...
            if vert not in visited:
                # Mark it as visited
                visited.add(vert)
                # Call dft_recursive on each neighbor
                if vert == destination_vertex:
                    path = v
                    print(path)
                    return path
                else:
                    if self.get_neighbors(vert):
                        for i in self.get_neighbors(vert):
                            if isinstance(v, list):
                                temp = v.copy()
                                temp.append(i)
                                s.push(temp)
                                self.dfs_recursive(temp, destination_vertex)
                            else:
                                temp = [vert]
                                temp.append(i)
                                self.dfs_recursive(temp, destination_vertex)
                    else:
                        return


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

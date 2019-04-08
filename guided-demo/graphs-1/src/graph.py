class Stack:
    def __init__(self):
        self.size = 0
        self.storage = list()

    def push(self, item):
        if item not in self.storage:
            self.storage.append(item)
            self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        return None

    def len(self):
        return self.size


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = list()

    def enqueue(self, item):
        if item not in self.storage:
            self.storage.append(item)
            self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(0)
        return None

    def len(self):
        return self.size


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
            # need to make this bi directional
        else:
            raise IndexError("That vertex does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exist, good sir!")
# implemnt the queue, and enque the starting Vertex ID

    def bfs(self, starting_vertex_id):
        # create a empty queue
        q = Queue()
        # create a set to store verticies
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
        # If that vertex has not been visited:
            # Mark it as visited
            print(v)
            visited.add(v)
            # Add all of its neighbors to the back of the queue
            for next_vert in self.vertices[v]:
                q.enqueue(next_vert)

    def dfs(self, starting_vertex_id):
        s = Stack()
        s.push(starting_vertex_id)
        visited = set()
        # while the queue is not empty
        while s.size() > 0:
            # dequeue the first vertex
            v = s.pop()
        # If that vertex has not been visited:
            # Mark it as visited
            print(v)
            visited.add(v)

            for next_vert in self.vertices[v]:
                s.push(next_vert)

"""
Simple graph implementation
"""


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

    # this is not how you define an edge! this is a vertex! right? i mean, i get it, but ... what?
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

    def bft(self, starting_vertex_id):
        # create a empty queue
        q = Queue()
        q.enqueue(starting_vertex_id)
        # create a set to store verticies
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            vertex = q.dequeue()
        # If that vertex has not been visited:
            if vertex not in visited:
                # Mark it as visited

                visited.add(vertex)
            # Add all of its neighbors to the back of the queue
                for next_vert in self.vertices[vertex]:
                    q.enqueue(next_vert)

    def dft(self, starting_vertex_id):
        s = Stack()
        s.push(starting_vertex_id)
        visited = set()
        # while the queue is not empty
        while s.size() > 0:
            # dequeue the first vertex
            vertex = s.pop()
        # If that vertex has not been visited:
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
            # Mark it as visited
                for next_vert in self.vertices[vertex]:
                    s.push(next_vert)
# working on traversal now
    # work on recursive version:

    def dft_recursive(self, vertex, visited=None):
        if visited == None:
            visited = set()

        # mark the starting vertex as visited
        visited.add(vertex)
        # call dft_recursive on all children
        for neighbor in self.vertices[vertex]:
            if neighbor not in visited:
                return self.dft_recursive(neighbor, visited)


# A PATH IS JUST AN ARRAY! DONT THING OF IT AS A STACK OR A QUEUE OR A SET. ITS JUST AN ARRAY


    def bfs(self, starting_vertex, target):
        # build an empty queue
        queue = Queue()

        # create a visited set
        visited = set()

        # enqueue [A Path To] the starting vertex to the queue
        queue.enqueue([starting_vertex])
        # while queue is not empty
        while queue.size() > 0:
            # dequeue the first [PATH] from the queue
            queue_in_check = queue.dequeue()
            # pull the last vertex from the path
            # check if it's visited...
            if queue_in_check[-1] not in visited:
                # add it to visited
                visited.add(queue_in_check[-1])
                # if it hasn't been visited
                if queue_in_check[-1] == target:
                    return queue_in_check  # you need to return the whole path for this section
                    # and we are done!

                for neighbor_vert in self.vertices[queue_in_check[-1]]:

                    # by value, not by ref - cool trick to copy a array
                    path = queue_in_check[:]
                    # append the neighbor vertex to the path
                    path.append(neighbor_vert)
                    # enqueue the new path
                    queue_in_check.enqueue(path)

    def dfs(self, starting_vertex, target):
        # use a stack instead of a queue, and it should actually all work out.
                # build an empty queue
        stack = Stack()

        # create a visited set
        visited = set()

        # enqueue [A Path To] the starting vertex to the queue
        stack.push([starting_vertex])
        # while queue is not empty
        while stack.size() > 0:
            # dequeue the first [PATH] from the queue
            stack_in_check = stack.pop()
            # pull the last vertex from the path
            # check if it's visited...
            if stack_in_check[-1] not in visited:
                # add it to visited
                visited.add(stack_in_check[-1])
                # if it hasn't been visited
                if stack_in_check[-1] == target:
                    return stack_in_check  # you need to return the whole path for this section
                    # and we are done!

                for neighbor_vert in self.vertices[stack_in_check[-1]]:

                    # by value, not by ref - cool trick to copy a array
                    path = stack_in_check[:]
                    # append the neighbor vertex to the path
                    path.append(neighbor_vert)
                    # enqueue the new path
                    stack_in_check.enqueue(path)

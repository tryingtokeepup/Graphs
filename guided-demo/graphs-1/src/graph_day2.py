import random

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def dft_r(self, start_vert, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vert)
        print(start_vert)
        # go through value of key start_vert, which is going to be in an array
        for child_vert in self.vertices[start_vert]:
            # if we haven't visited the vertix, we need to recursively visit that node
            if child_vert not in visited:
                self.dft_r(child_vert, visited)

    def bfs_path(self, start_vertex_id, target_value):
        q = Queue()
        q.enqueue([start_vertex_id])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v not in visited:
                if v == target_value:
                    return path
                visited.add(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None

    def dfs_r_path(self, start_vert, target_value, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(start_vert)
        path = path + [start_vert]
        if start_vert == target_value.value:
            return path
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                new_path = self.dfs_r_path(
                    child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None


class SocialGraph:
    def __init__(self, lastID = 0, users = {}, friendships= {}):
        self.lastID = lastID
        self.users = {}
        self.friendships = friendships
    
    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def addFriendship(self, userID, friendID):
        # adding a edge between two vertices
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)



    
    def populateGraph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}


        # Add users
        for user in range(num_users):
            self.addUser("User %s" % user) # user 0, user 1, user 2


        # Create friendships
        
        # Generate all possible friendship combinations
        possible_friendships = []
        # avoid dups by making sure that the first id is higher than the 2nd id
        for user_id in self.users:
            for other_id in range(user_id + 1, self.lastID + 1):
                    possible_friendships.append(user_id, other_id)
        
        random.shuffle(possible_friendships)

        # Create friendships(edges) for the first X tuples of the list
	    # X is determined by the formula: numUsers * avgFriendships // 2
	    # Need to divide by 2 since each addFriendship() creates 2 friendships
        for i in range((num_users * avg_friendships) //2 ):
            friendship = possible_friendships[i]
            self.addFriendship(friendship[0], friendship[1])
        


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        relationships = self.users(userID)
        return visited


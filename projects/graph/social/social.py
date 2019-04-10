import random


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


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

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
            self.addUser("User %s" % user)  # user 0, user 1, user 2

        # Create friendships

        # Generate all possible friendship combinations
        possible_friendships = []
        # avoid dups by making sure that the first id is higher than the 2nd id
        for user_id in self.users:
            for other_id in range(user_id + 1, self.lastID + 1):
                possible_friendships.append((user_id, other_id))

        random.shuffle(possible_friendships)

        # Create friendships(edges) for the first X tuples of the list
        # X is determined by the formula: numUsers * avgFriendships // 2
        # Need to divide by 2 since each addFriendship() creates 2 friendships
        for i in range((num_users * avg_friendships) // 2):
            friendship = possible_friendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def bfs(self, starting_vertex, target):
            # Create an empty queue
        # q = Queue()
        # # Create an empty set of visited vertices
        # visited = set()
        # # Put the starting vertex in our Queue
        # q.enqueue([starting_vertex])
        # # While the queue is not empty....
        # while q.size > 0:
        #     path = q.dequeue()
        #     # Dequeue the first node from the queue
        #     v = path[-1]
        #     # If that node has not been visted...
        #     if v not in visited:
        #         # Mark it as visited
        #         visited.add(v)
        #         if v == search_vertex:
        #             return path
        queue = Queue()

        # create a visited set
        visited = set()

        # enqueue [A Path To] the starting vertex to the queue
        queue.enqueue([starting_vertex])
        # while queue is not empty
        while queue.size > 0:
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
                # Then, put all of it's children into the queue
                for neighbor in self.friendships[queue_in_check[-1]]:
                    path = queue_in_check[:]
                    path.append(neighbor)
                    queue.enqueue()

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        print(f"user ID {userID}")

        for i in range(1, len(self.users)):
            visited[i] = self.bfs(userID, i)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(3)
    print(connections)

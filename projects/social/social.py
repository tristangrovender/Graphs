from util import Queue
import random


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
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

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
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
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(numUsers):
            self.addUser(user)

        # Create friendships
        friendship_combinations = []
        ## make all possible friendship combinations 
        for userId in self.users:
            for friendID in range(userId + 1, self.lastID+1):
                friendship_combinations.append((userId, friendID))
        ## shuffle the friendship combinations
        random.shuffle(friendship_combinations)
        ## take the N number of friendships
        totalFriendships = avgFriendships * numUsers
        # averageFriendShips = totalFriendShips / numUsers
        friendships_to_make = friendship_combinations[:(totalFriendships / 2)]

        for friendship in friendships_to_make:
            first_friend = friendship[0]
            second_friend = friendship[1]
            self.addFriendship(first_friend,second_friend)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        path = [userID]
        q.enqueue(path)
        while q.size():
            path = q.dequeue()
            node = path[-1]
            if node not in visited:
                visited[node] = path
                for friend in self.friendships[node]:
                    path_copy = path[:]
                    
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

# breath first search

# keep a queue containing people to check
# pop off first person
# check if that person is a mango seller
# if yes - you're done
# if no - add al their neighbors to queue
# loop
# if the queue is empty there are no sellers

# push == enqueue and pop == dequeue

from collections import deque

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    # creates a new queue
    search_queue = deque()
    # Adds all of your neighbors to the search queue
    search_queue += graph[name]
    # keep track of who has been searched
    searched = []
    # while queue isn't empty
    while search_queue:
        # popleft grabs the first person off the queue
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == 'm'


print(search("you"))

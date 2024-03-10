graph = {}

graph["you"] = ["alice", "clear", "bob"]
graph["bob"] = ["anuj", "peggi"]
graph["clear"] = ["tom", "jonny"]
graph["alice"] = ["peggi"]
graph["peggi"] = []
graph["anuj"] = []
graph["jonny"] = []
graph["tom"] = []

def check_mango_seller(name):
    return name[-1]  == "m"

from collections import deque

research_queue = deque()
research_queue += graph["you"]

while research_queue:
    people = research_queue.popleft()
    if check_mango_seller(people):
        print(people + " is mango seller")
    else:
        research_queue += graph[people]




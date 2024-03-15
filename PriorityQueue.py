# Author Alex Hemmerlin
# this file implements a priority queue

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, item: tuple[Any, int]):
        self.queue.append(item)

    def dequeue(self) -> tuple[Any, int]:
        highestPriority = self.queue[0][1]
        returnVal = self.queue[0]
        for val in self.queue:
            if val[1] > highestPriority:
                highestPriority = val[1]
                returnVal = val
        self.queue.remove(returnVal)
        return returnVal
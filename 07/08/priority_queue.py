import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def enqueue(self, item, priority):
        heapq.heappush(self.elements, (-priority, item))

    def dequeue(self):
        return heapq.heappop(self.elements)[1]
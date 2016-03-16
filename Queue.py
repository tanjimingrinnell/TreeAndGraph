from collections import deque

class Queue:

    queue = []

    def __init__(self):
        self.queue = []

    def enqueue(self, inputValue):
        self.queue.append(inputValue)

    """Returns a value"""
    def dequeue(self):
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def clear(self):
        self.queue = []
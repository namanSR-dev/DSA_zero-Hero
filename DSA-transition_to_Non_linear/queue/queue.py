from collections import deque

class Queue:
    def __init__(self):
        # Double underscores make this attribute private
        self.__q = deque()

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise."""
        return not self.__q

    def dequeue(self):
        """Removes and returns the front item. Returns None if empty."""
        if self.is_empty():
            return None
        return self.__q.popleft()
    
    def enqueue(self, val: int) -> None:
        """Adds an item to the rear of the queue."""
        self.__q.append(val)

    def peek(self):
        """Returns the front item without removing it. Returns None if empty."""
        if self.is_empty():
            return None
        return self.__q[0]
    
    def size(self) -> int:
        """Returns the total number of items in the queue."""
        return len(self.__q)
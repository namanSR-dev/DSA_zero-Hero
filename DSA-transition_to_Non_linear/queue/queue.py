from collections import deque

class queue:
    def __init__(self):
        self.__q = deque()

    def isEmpty(self):
        return not self.__q


    def deque(self):
        if not self.__q:
            return None
        
        return self.__q.popleft()
    
    def enqueue(self, val:int):
        self.__q.append(val)

    def seek(self):
        if not self.__q:
            return None
        return self.__q[0]
    
    def size(self):
        if not self.__q:
            return 0
        
        return len(self.__q)
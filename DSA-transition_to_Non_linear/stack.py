class Stack :
    def __init__ (self):
        self.__data = []
    
    def push(self, x):
        self.__data.append(x)
    
    def pop(self):
        if not self.__data:
            return None
        else: 
            return self.__data.pop()
        
    def peek(self):
        if not self.__data:
            return None
        return self.__data[-1]
    
    def is_empty(self):
        return not self.__data
    
    def size(self):
        return len(self.__data)

class Queue:

    def __init__(self, max_size=10):
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__data = []


    def enqueue(self, o):
        if self.is_full():
            raise IndexError("Queue is full!")

        self.__data.append(o)

        self.__tail += 1


    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")

        self.__tail -= 1
        return self.__data[self.__tail]



    def is_empty(self):
        return self.__head == self.__tail



    def is_full(self):
        return self.__tail == self.__max_size


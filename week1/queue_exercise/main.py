from queue import Queue


class Reverser:

    def __init__(self, input_string):

        self.__input_string = input_string

    def reverse(self):

        queue = Queue()

        for string in self.__input_string.split(" "):
            queue.enqueue(string)

        r = ""

        while not queue.is_empty():
            r += queue.dequeue() + " "

        return r.strip()


if __name__ == "__main__":
    while True:
        sentence = input("Enter a string: ")
        if sentence == "":
            break

        reverser = Reverser(sentence)
        print(reverser.reverse())






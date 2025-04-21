class Stack:

    def __init__(self):
        self.array = []

    def push(self, c):
        self.array.append(c)

    def pop(self):
        return self.array.pop()

    def top(self):
        return self.array[len(self.array) - 1]

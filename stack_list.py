class Stack_List:
    def __init__(self):
        self.storage = []

    def add(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()

stack = Stack_List()
stack.add(5)
stack.add(15)
stack.add(45)
print(stack.pop())
print(stack.pop())
print(stack.pop())

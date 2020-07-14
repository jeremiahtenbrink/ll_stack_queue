from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def add(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_tail()

    def print_stack(self):
        pass

stack = Stack()
stack.add(5)
stack.add(53)
stack.add(52)
print(stack.pop())
print(stack.pop())
print(stack.pop())
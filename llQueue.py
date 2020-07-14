from linked_list import LinkedList

class LL_Queue:
    def __init__(self):
        self.storage = LinkedList()

    def enqueue(self, data):
        self.storage.add_to_tail(data)

    def dequeue(self):
        return self.storage.remove_head()

q = LL_Queue()
q.enqueue(5)
q.enqueue(50)
q.enqueue(20)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
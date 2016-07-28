class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def is_empty(self):
        if len(self.items) > 0:
            return False
        return True

    def size(self):
        return len(self.items)

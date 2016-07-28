class Dequeue(object):
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        del self.items[0]

    def remove_rear(self):
        self.items.pop()

    def is_empty(self):
        if len(self.items) > 0:
            return False
        return True

    def size(self):
        return len(self.items)

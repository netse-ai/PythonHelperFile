class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if len(self.items) > 0:
            return False
        return True

    def size(self):
        return len(self.items)


stack = Stack()
stack.push("Dog")
stack.push("Cat")
stack.peek()
stack.is_empty()
stack.size()
stack.pop()
stack.size()

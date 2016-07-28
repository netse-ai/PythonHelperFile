class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if len(self.items) > 0:
            return False
        return True

    def size(self):
        return len(self.items)


# stack = Stack()
# stack.push("Dog")
# stack.push("Cat")
# print stack.peek()
# print stack.is_empty()
# print stack.size()
# stack.pop()
# print stack.size()
# stack.pop()
# print stack.size()
# stack.pop()
# print stack.size()

def par_checker(symbol):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbol) and balanced:
        sign = symbol[index]
        if sign == '(':
            s.push(sign)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def binary_string(decNumber):

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        # print remstack.items
        decNumber = decNumber // 2

    output = ""
    for i in range(len(remstack.items)):
        output += str(remstack.items[i])

    return output

print binary_string(8)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def set_data(self, new_data):
        self.data = new_data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next



class UlList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def index(self, item):
        current = self.head
        count = 0
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
                return count
            else:
                count += 1
                current = current.get_next()
        if found == False:
            return found
        else:
            return count

    def append(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.get_next()
            if previous.get_next() == None:
                previous.set_next(temp)

    def pop(self):
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.get_next()
            if previous.get_next() == None:
                self.remove(previous.data)

    def return_all(self):
        current = self.head
        items = []
        while current != None:
            items.append(current.data)
            current = current.get_next()
        return items


ul = UlList()
ul.add("dog")
ul.add("frog")
ul.add("fg")
print ul.return_all()
print ul.head.data
print ul.size()
print ul.search("rog")
ul.remove('fg')
ul.add("fg")
print ul.return_all()
print ul.index("frog")
ul.append("monkey")
print ul.search("monkey")
print ul.return_all()
print ul.pop()
print ul.return_all()

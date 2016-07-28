class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next



class OlList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
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

ol = OlList()

ol.add(1)
ol.add(3)
ol.add(2)

print ol.return_all()
ol.remove(3)
print ol.return_all()

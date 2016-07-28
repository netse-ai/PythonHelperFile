class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def set_next(self, new_next):
        self.next = new_next

    def set_data(self, new_data):
        self.data = new_data

class Olist(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def find(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return current.data
            else:
                current = current.get_next()
        return False

    def return_all(self):
        items = []
        current = self.head
        while current != None:
            items.append(current.data)
            current = current.get_next()
        return items

    def delete(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



olist = Olist()
olist.add("Dog")
olist.add("grof")
olist.add("tdog")
print olist.return_all()
print olist.find("dog")
olist.delete("tdog")
olist.delete("Dog")
print olist.return_all()

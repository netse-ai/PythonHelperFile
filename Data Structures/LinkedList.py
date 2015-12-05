import pytest

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())





def main():
    l_list = LinkedList()
    l_list.insert("David")
    assert l_list.head.get_data() == "David"
    assert l_list.head.get_next() is None



def test_insert_two():
    l_list = LinkedList()
    l_list.insert("David")
    l_list.insert("Thomas")
    assert l_list.head.get_data() == "Thomas"
    head_next = l_list.head.get_next()
    assert head_next.get_data() == "David"


def test_nextNode():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    assert l_list.head.get_data() == "Rasmus"
    head_next = l_list.head.get_next()
    assert head_next.get_data() == "Pallymay"
    last = head_next.get_next()
    assert last.get_data() == "Jacob"


def test_positive_search():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    found = l_list.search("Jacob")
    assert found.get_data() == "Jacob"
    found = l_list.search("Pallymay")
    assert found.get_data() == "Pallymay"
    found = l_list.search("Jacob")
    assert found.get_data() == "Jacob"


def test_searchNone():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    # make sure reg search works
    found = l_list.search("Jacob")
    assert found.get_data() == "Jacob"
    with pytest.raises(ValueError):
        l_list.search("Vincent")


def test_delete():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    l_list.delete("Rasmus")
    assert l_list.head.get_data() == "Pallymay"
    l_list.delete("Jacob")
    assert l_list.head.get_next() is None


def test_delete_value_not_in_list():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    with pytest.raises(ValueError):
        l_list.delete("Sunny")


def test_delete_empty_list():
    l_list = LinkedList()
    with pytest.raises(ValueError):
        l_list.delete("Sunny")


def test_delete_next_reassignment():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Cid")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    l_list.delete("Pallymay")
    l_list.delete("Cid")
    assert l_list.head.next_node.get_data() == "Jacob"

test_delete_empty_list()

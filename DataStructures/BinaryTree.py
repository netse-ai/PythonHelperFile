class BinaryTree(object):
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new):
        if self.left_child == None:
            self.left_child = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new):
        if self.right_child == None:
            self.right_child = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

r = BinaryTree('a')
print r.get_root_val()
r.insert_left('b')
print r.get_left_child().get_root_val()
r.insert_right('c')
r.get_right_child().insert_right('f')
print r.get_right_child().get_root_val()
r.get_right_child().get_right_child().insert_right(r)
z = r.get_right_child().get_right_child().get_right_child().get_root_val()
print z.get_root_val()
t = z.get_right_child().get_right_child().get_right_child().get_root_val()
# print y.get_root_val()
# print r
while r.right_child != None:
    y = r.get_right_child()
    print y.key
    # if y.get_right_child() != None:
    r = y.get_right_child()
    print r.key

tree = ['a', #root
        ['b', #left subtree
        ['d', [], []],
        ['e', [], []] ],
        ['c', #right subtree
        ['f', [], []],
        ['g', [], []], ]
        ]

# print tree[2]

def binary_list(r):
    return [r, [], []]

def insert_left(root, new):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new, t, []])
    else:
        root.insert(1, [new, [], []])
    return root

def insert_right(root, new):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new, t, []])
    else:
        root.insert(2, [new, [], []])
    return root

tree = binary_list(3)
print tree
insert_left(tree, 4)
70insert_right(tree, 5)
print tree

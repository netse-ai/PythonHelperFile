import json

class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected_to' + str([x.id for x in self.connected_to])

    def get_id(self):
        return self.id

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph(object):
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

g = Graph()
for i in range(14):
    g.add_vertex(i)

obj = {'attackspeed': 5}

class Node(object):
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def __str__(self):
        return self.name


class Build(object):
    def __init__(self):
        self.attackspeed = 3

    def add_stats(self, n):
        # for i in n:
        if n['attackspeed']:
            # if n[i] == 'attackspeed':
            self.attackspeed += n['attackspeed']
            # else:
            #     print "no such stat"

    def return_stats(self):
        return self.attackspeed


#
# b = Build()
# node0 = Node(5, obj)
# # node1 = Node(5)
# # node2 = Node(1)
# # node3 = Node(1)
# if node0.rank == 4:
#     b.add_stats(node0.data)
#     g.add_edge(0, 2)
#     print b.return_stats()
# else:
#     print "%r" % (node0.rank)
#
#
# for v in g:
#     for w in v.get_connections():
#         print "(%s, %s)" % (v.get_id(), w.get_id())



class Graph(object):
    def __init__(self):
        self.edges = {}

    def neighbors(self, num):
        return self.edges[num]

    def add_neighbor(self, node1=None, node2=None, node3=None, node4=None):
        if node1 == None:
            print "Something went terribly wrong!"
        elif node1 != None and node2 == None and node3 == None and node4 == None:
            self.edges.update({node1:["End of Graph"]})
        elif node4 == None:
            self.edges.update({node1:[node2, node3]})
        else:
            self.edges.update({node1: [node2, node3, node4]})



node0 = Node('Mastery1', 5)
node1 = Node('Mastery2', 0)
node2 = Node('Mastery3', 1)
node3 = Node('Mastery4', 0)
node4 = Node('Mastery5', 0)
node5 = Node('Mastery6', 5)
node6 = Node('Mastery7', 0)
node7 = Node('Mastery8', 1)
node8 = Node('Mastery9', 0)
node9 = Node('Mastery10', 5)
node10 = Node('Mastery11', 0)
node11 = Node('Mastery12', 0)
node12 = Node('Mastery13', 0)
node13 = Node('Mastery14', 1)



graf = Graph()
graf.edges = {
    # node0.name:[node2.name, node3.name, node4.name],
    # node1.name:[node2.name, node3.name, node4.name],
    # node2.name:[node5.name, node6.name],
    # node3.name:[node5.name, node6.name],
    # node4.name:[node5.name, node6.name],
    # node5.name:[node7.name, node8.name],
    # node6.name:[node7.name, node8.name],
    # node7.name:[node9.name, node10.name],
    # node8.name:[node9.name, node10.name],
    # node9.name:[node11.name, node12.name, node13.name],
    # node10.name:[node11.name, node12.name, node13.name]
    # 'A': ['B'],
    # 'B': ['A', 'C', 'D'],
    # 'C': ['A'],
    # 'D': ['E', 'A'],
    # 'E': ['B']
}
if node0.rank == 5 and node1.rank != 5:
    graf.add_neighbor(node0.name, node2.name, node3.name, node4.name)
elif node1.rank == 5 and node0.rank != 5:
    graf.add_neighbor(node1.name, node2.name, node3.name, node4.name)
elif node1.rank + node0.rank == 5:
    graf.add_neighbor(node0.name, node2.name, node3.name, node4.name)
    graf.add_neighbor(node1.name, node2.name, node3.name, node4.name)

if node2.rank == 1 and node3.rank != 1 and node4.rank != 1:
    graf.add_neighbor(node2.name, node5.name, node6.name)
elif node3.rank == 1 and node2.rank != 1 and node4.rank != 1:
    graf.add_neighbor(node3.name, node5.name, node6.name)
elif node4.rank == 1 and node2.rank != 1 and node3.rank != 1:
    graf.add_neighbor(node4.name, node5.name, node6.name)

if node5.rank == 5 and node6.rank != 5:
    graf.add_neighbor(node5.name, node7.name, node8.name)
elif node6.rank == 5 and node6.rank !=5:
    graf.add_neighbor(node6.name, node7.name, node8.name)

if node7.rank == 1 and node8.rank != 5:
    graf.add_neighbor(node7.name, node9.name, node10.name)
elif node8.rank == 1 and node8.rank != 1:
    graf.add_neighbor(node8.name, node9.name, node10.name)

if node9.rank == 5 and node10.rank != 5:
    graf.add_neighbor(node9.name, node11.name, node12.name, node13.name)
elif node10.rank == 5 and node9.rank != 5:
    graf.add_neighbor(node10.name, node11.name, node12.name, node13.name)

if node11.rank == 1 and node12.rank != 1 and node13.rank != 1:
    graf.add_neighbor(node11.name)
elif node12.rank == 1 and node11.rank != 1 and node13.rank != 1:
    graf.add_neighbor(node12.name)
elif node13.rank == 1 and node12.rank != 1 and node11.rank != 1:
    graf.add_neighbor(node13.name)


print json.dumps(graf.edges, indent=4, sort_keys=True)

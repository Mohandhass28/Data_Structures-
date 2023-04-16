class Node:
    def __init__(self,val):
        self.data = val
        self.parent = None
        self.right = None
        self.left = None
class splaytree:
    def __init__(self):
        self.root = None

    def splay(self,node):


    def insert(self,val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        y = None
        x = self.root
        while x != None:
            y = x
            if x.data < node.data:
                x = x.right
            else:
                x= x.left
        node.parent = y

        if y.data < node.data:
            y.right = node
        else:
            y.left = node


tree = splaytree()
tree.insert(4)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(9)
tree.insert(6)
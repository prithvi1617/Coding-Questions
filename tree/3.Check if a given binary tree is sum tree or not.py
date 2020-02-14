
class Node:
    def __init__(self,data):
        self.left=self.right = None
        self.data = data


def sumn(node):
    if node == None:
        return 0
    return (sumn(node.left)+node.data+sumn(node.right))
def sumt(nodee):
    if nodee == None:
        return 1
    if nodee.left == None and nodee.right==None:
        return 1
    ls=sumt(nodee.left)
    rs=sumt(nodee.right)
    if (nodee.data) == ls+rs:
        if sumt(nodee.left) and sumt(nodee.right):
            return 1
tree = Node(8)
tree.left = Node(3)
tree.right = Node(2)
tree.left.left = Node(2)
tree.left.right = Node(1)

if (sumt(tree)):
    print('yes')
else:
    print('no')

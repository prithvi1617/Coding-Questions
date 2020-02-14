class Node:
    def __init__ (self,data):
        self.left=self.right= None
        self.data = data


def inorder(node):
    if (node==None):
        return
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

def postorder(node):
    if node==None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' ')

def preorder(node):
    if node==None:
        return 
    print(node.data , end=' ')
    preorder(node.left)
    preorder(node.right)
    
inorder(tree)
print(' ')
postorder(tree)
print( ' ')
preorder(tree)


class node:
    def __init__(self,data):
        self.left=self.right = None
        self.data = data

def mirror(node):
    temp=node
    if node==None:
        return
    mirror(node.left)
    mirror(node.right)
    temp = node.left
    node.left  =node.right
    node.right = temp
    
def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.data , end=' ')
    inorder(node.right)

tree = node(1)
tree.left = node(2)
tree.right = node(3)
tree.left.left = node(4)
tree.left.right = node(5)

inorder(tree)
mirror(tree)
print(' ')
inorder(tree)

class node:
    def __init__(self,data):
        self.left=self.right =None
        self.data = data
s=[]
def rtl(node):
    if (node==None):
        return 1
    
    s.append(node.data)
    rtl(node.left)
    if(node.left is None and node.right is None):
        print(s)
    rtl(node.right)

    s.pop()



tree = node(1)
tree.left = node(2)
tree.right = node(3)
tree.left.left = node(4)
tree.left.right = node(5)

rtl(tree)
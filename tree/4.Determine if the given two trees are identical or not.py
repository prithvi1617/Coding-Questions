

class node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
def identical(t1,t2):
    if t1 is None and t2 is None:
        return 1
    elif(t1.data==t2.data):
        if(identical(t1.left,t2.left) and identical(t1.right,t2.right)):
            return 1
    return 0

tree1 = node(1)
tree1.left = node(2)
tree1.right = node(3)
tree1.left.left = node(4)
tree1.left.right = node(5)

tree = node(1)
tree.left = node(2)
tree.right = node(3)
tree.left.left = node(4)
tree.left.right = node(5)

if(identical(tree,tree1)):
    print('yes')
else:
    print('no')
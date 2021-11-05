"""
Tree implementation with class
"""

class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, node):
        if self.leftChild == None:
            self.leftChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, node):
        if self.rightChild == None:
            self.rightChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, val):
        self.key = val

    def getRootVal(self):
        return self.key

    def __str__(self):
        rightKey = self.rightChild.key if self.rightChild else "None"
        leftKey = self.leftChild.key if self.leftChild else "None"
        return f"^key:{self.key}# ^left:key:{leftKey}# ^right:key:{rightKey}#"

def preorder(tree):
    print(tree)
    if tree.leftChild:
        preorder(tree.leftChild)
    if tree.rightChild:
        preorder(tree.rightChild)

def postorder(tree):
    if tree.leftChild:
        postorder(tree.leftChild)
    if tree.rightChild:
        postorder(tree.rightChild)
    print(tree)

def inorder(tree):
    if tree.leftChild:
        inorder(tree.leftChild)
    print(tree)
    if tree.rightChild:
        inorder(tree.rightChild)



r = BinaryTree("God")
r.insertLeft('Brandon')
r.insertRight('Dani')

b = r.getLeftChild()
b.insertLeft("Haley")
b.insertRight("Austin")

print("------------------------------------------------")
preorder(r)
print("------------------------------------------------")
postorder(r)
print("------------------------------------------------")
inorder(r)

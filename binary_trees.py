class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

#to find out if a value is in a BINARY SEARCH TREE
# findval method to compare the value with nodes
    '''
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
    '''

    #Binary Tree Traversal
    def inOrderTraversal(self):
        if self.left != None:
            self.left.inOrderTraversal()
        if self.data != None:
            print(self.data)
        if self.right != None:
            self.right.inOrderTraversal()

    def preOrderTraversal(self):
        if self.data != None:
            print(self.data)
        if self.left != None:
            self.left.inOrderTraversal()
        if self.right != None:
            self.right.inOrderTraversal()    
    
    def PostOrderTraversal(self):
        if self.left != None:
            self.left.inOrderTraversal()
        if self.right != None:
            self.right.inOrderTraversal()   
        if self.data != None:
            print(self.data)

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PostOrderTraversal()


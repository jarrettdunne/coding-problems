# This problem was asked by Microsoft.

# Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

#   1
#  / \
# 2   3
#    / \
#   4   5

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
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

    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()

if __name__ == "__main__":
    node = Node(1)
    for i in range(2,6):
        print(i)
        node.insert(i)
        
    # node.show()


class Node:
    
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

    def insert_node(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

    def find_elem(self, s_elem):
        if self.data:
            if s_elem == self.data:
                return 'FOUND'
            elif s_elem < self.data:
                return self.left.find_elem(s_elem)
            elif s_elem > self.data:
                return self.right.find_elem(s_elem)
        return 'NF' 

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
        return

    def printTreeReverse(self):
        if self.right:
            self.right.printTreeReverse()
        print(self.data)
        if self.left:
            self.left.printTreeReverse()
        return


if __name__ == '__main__':
    bst = Node(5)
    bst.insert_node(7)
    bst.insert_node(13)
    bst.insert_node(80)
    bst.insert_node(8)
    bst.insert_node(16)
    bst.insert_node(11)
    # print(bst.find_elem(6))
    # bst.printTree()
    bst.printTreeReverse()

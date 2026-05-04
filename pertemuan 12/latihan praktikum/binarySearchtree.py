class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearhTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Langkah 1
        new = Node(data)

        # Langkah 2
        if self.root == None:
            # Jika iya
            self.root = new
            return
        
        # Jika tidak
        # Langkah 3
        P = self.root
        Q = self.root

        #langkah 4
        while Q != None and new.data != P.data:
            #langkah 5
            P = Q

            # Langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right

        # Langkah 7
        if new.data == P.data:
            # Jika iya
            print("Data duplikat")
            return
            
        # Jika tidak
        # Langkah 8
        if new.data < P.data:
            # Jika iya
            P.left = new
        # Jika tidak
        else:
            P.right = new
        # Selesai

bst = BinarySearhTree()

bst.insert(12)
bst.insert(9)
bst.insert(99)
bst.insert(67)
bst.insert(35)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)

in_order(bst.root)


class Node:
    """Representasi satu node dalam Binary Tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Implementasi Binary Tree"""

    def __init__(self):
        self.root = None

    def insert_root(self, data):
        """Memasukkan node root"""
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        """Memasukkan child kiri dari suatu node"""
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        """Memasukkan child kanan dari suatu node"""
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

bst = BinaryTree()

bst.insert_root('F')
bst.insert_left(bst.root, 'B')
bst.insert_right(bst.root, 'G')
bst.insert_left(bst.root.left, 'A')
bst.insert_right(bst.root.left, 'D')
bst.insert_left(bst.root.left.right, 'C')
bst.insert_right(bst.root.left.right, 'E')
bst.insert_right(bst.root.right, 'I')
bst.insert_left(bst.root.right.right, 'H')

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

inorder(bst.root)

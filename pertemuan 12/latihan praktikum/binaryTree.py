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

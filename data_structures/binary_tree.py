class BinaryTree:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

    def __str__(self):
        return str(self.data)

    def left_child(self):
        return self.left

    def right_child(self):
        return self.right

    def set_node_data(self, data):
        self.data = data

    def node_data(self):
        return self.data

    def insert_right_child(self, data):
        if not self.right:
            self.right = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.right = self.right
            self.right = tree

    def insert_left_child(self, data):
        if not self.left:
            self.left = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.left = self.left
            self.left = tree
    
    def height(self, tree):
        if not tree.data:
            return 0

        return 1 + max(height(tree.left), height(tree.right))

    def preorder_traversal(self, tree, func):
        if not tree:
            return

        func(tree)
        self.preorder_traversal(tree.left, func)
        self.preorder_traversal(tree.right, func)

    def inorder_traversal(self, tree, func):
        if not tree:
            return

        self.inorder_traversal(tree.left, func)
        func(tree)
        self.inorder_traversal(tree.right, func)

    def postorder_traversal(self, tree, func):
        if not tree:
            return

        self.postorder_traversal(tree.left, func)
        self.postorder_traversal(tree.right, func)
        func(tree)


class BinaryTree:
    def __init__(self, root):
      self.left = None
      self.right = None
      self.root = root

    def insert_right_child(self, root):
        if not self.right:
            self.right = BinaryTree(root)
        else:
            tree = BinaryTree(root)
            tree.right = self.right
            self.right = tree

    def insert_left_child(self, root):
        if not self.left:
            self.left = BinaryTree(root)
        else:
            tree = BinaryTree(root)
            tree.left = self.left
            self.left = tree

    def __str__(self):
        return str(self.root)


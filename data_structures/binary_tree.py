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


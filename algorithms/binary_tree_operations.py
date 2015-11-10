class BinaryTreeOperation(object):
    def min_depth(self, T):
        if not T:
            return 0

        return 1 + min(self.max_depth(T.left), self.max_depth(T.right))

    def max_depth(self, T):
        if not T:
            return 0

        return 1 + max(self.max_depth(T.left), self.max_depth(T.right))

    def is_balanced(self, T):
        """
        A tree is considered balanced if it the difference between the maximum
        depth and the minimum depth is less than or equal to 1.
        """
        return self.max_depth(T) - self.min_depth(T) <= 1

    def preorder(self, T, func):
        if not T:
            return

        func(T)
        preorder(T.left)
        preorder(T.right)

    def inorder(self, T, func):
        if not T:
            return

        preorder(self, T.left)
        func(T)
        preorder(T.right)

    def postorder(self, T, func):
        if not T:
            return

        preorder(T.left)
        preorder(T.right)
        func(T)

    def invert(self, T):
        if not T:
            return T

        temp = T.left
        T.left = invert(T.right)
        T.right = invert(temp)

    def print_tree(self, T, indent=0):
        if not T:
            return

        print('  ' * indent + T.root)

        self.print_tree(T.left, indent + 1)
        self.print_tree(T.right, indent + 1)


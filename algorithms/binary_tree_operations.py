class BinaryTreeOperation(object):

    def height(self, T):
        if not T:
            return 0

        return 1 + max(self.height(T.left), self.height(T.right))

    def is_balanced(self, T):
        if not T:
            return True

        balanced = self.is_balanced(T.left) and self.is_balanced(T.right)
        height_difference = abs(self.height(T.left) - self.height(T.right))

        return balanced and height_difference <= 1

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
            return

        temp = T.left
        T.left = invert(T.right)
        T.right = invert(temp)


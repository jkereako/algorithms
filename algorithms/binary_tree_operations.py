class BinaryTreeOperation(object):
    def height(T):
        if not T.root:
            return 0

        return 1 + max(height(T.left), height(T.right))

    def preorder(T, func):
        if not T:
            return

        func(T)
        preorder(T.left)
        preorder(T.right)

    def inorder(T, func):
        if not T:
            return

        preorder(T.left)
        func(T)
        preorder(T.right)

    def postorder(T, func):
        if not T:
            return

        preorder(T.left)
        preorder(T.right)
        func(T)

    def invert(T):
        if not T:
            return

        temp = T.left
        T.left = invert(T.right)
        T.right = invert(temp)


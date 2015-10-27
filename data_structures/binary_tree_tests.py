from binary_tree import BinaryTree
import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree('Aegon')
        self.tree.insert_left_child('Rhaelle')
        self.tree.insert_right_child('Jaehaerys')
        self.tree.insert_left_child('Steffon')
        self.tree.insert_right_child('Rhaella')
        self.tree.insert_left_child('Robert I')

    def test_inorder(self):
        def func(data):
            print(data)

        BinaryTree.inorder_traversal(self.tree, func)

if __name__ == '__main__':
    unittest.main()

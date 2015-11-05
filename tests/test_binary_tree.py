import algorithms
import data_structures
from algorithms import binary_tree_operations
from data_structures import binary_tree
import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = binary_tree.BinaryTree('Aegon')
        self.tree.insert_left_child('Rhaelle')
        self.tree.insert_right_child('Jaehaerys')
        self.tree.insert_left_child('Steffon')
        self.tree.insert_right_child('Rhaella')
        self.tree.insert_left_child('Robert I')

#    def test_inorder(self):
#        def func(data):
#            print(data)
#
#        binary_tree.BinaryTree.inorder_traversal(self.tree, func)


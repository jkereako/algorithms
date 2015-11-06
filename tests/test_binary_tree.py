import algorithms
import data_structures
from algorithms import binary_tree_operations
from data_structures import binary_tree
import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.operations = binary_tree_operations.BinaryTreeOperation()
        self.tree = binary_tree.BinaryTree('Aegon')
        self.tree.insert_left_child('Rhaelle')
        self.tree.insert_right_child('Jaehaerys')
        self.tree.insert_left_child('Steffon')
        self.tree.insert_right_child('Rhaella')

    def tearDown(self):
        self.tree = None

    def test_tree_height(self):
        result = self.operations.height(self.tree)
        self.assertTrue(result == 3)

    def test_tree_is_balanced(self):
        result = self.operations.is_balanced(self.tree)
        self.assertTrue(result)

    def test_tree_is_not_balanced(self):
        self.tree.insert_left_child('Robert I')

        result = self.operations.is_balanced(self.tree)
        self.assertFalse(result)

    def test_tree_inversion(self):
        self.operations.print_tree(self.tree)
        print("      Inverting...")
        tree = self.operations.invert(self.tree)
        self.operations.print_tree(tree)
      #  print(self.tree)


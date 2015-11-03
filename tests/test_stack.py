import data_structures
from data_structures import stack
import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = stack.Stack()

    def tearDown(self):
        self.stack = None

    def test_push(self):
        self.stack.push(77)
        self.assertTrue(self.stack.peek == 77)

        self.stack.push(15)
        self.assertTrue(self.stack.peek == 15)


import algorithms
from algorithms import binary_search
import unittest

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.list = [i for i in range(10000)]
        self.high = len(self.list) - 1
        self.low = 0

    def test_for_element_in_list(self):
        found = binary_search.binary_search(self.list, 69)

        self.assertTrue(found)

    def test_for_element_not_in_list(self):
        found = binary_search.binary_search(self.list, 100001)

        self.assertFalse(found)

    def test_list_of_one_element(self):
        self.list = [1]
        found = binary_search.binary_search(self.list, 1)

        self.assertTrue(found)

    def test_empty_list(self):
        self.list = []
        found = binary_search.binary_search(self.list, 1)

        self.assertFalse(found)


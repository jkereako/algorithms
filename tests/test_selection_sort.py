from algorithms import selection_sort
import unittest

class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.list = [9, 21, 3, 19, 290, 39, 343, 1 , 4, 6, 64, 3, 2, 13]
        self.expected = [1, 2, 3, 3, 4, 6, 9, 13, 19, 21, 39, 64, 290, 343]

    def test_sort(self):
        selection_sort.sort(self.list)
        self.assertTrue(self.list == self.expected)


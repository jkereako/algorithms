import algorithms
from algorithms import breadth_first_search
import unittest

class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.adjacency_list = {
                '1': ['2', '3', '4'],
                '2': ['5', '6'],
                '5': ['9', '10'],
                '4': ['7', '8'],
                '7': ['11', '12']
                }

    def test_stuff(self):
        print breadth_first_search.search(self.adjacency_list, '4', '10')

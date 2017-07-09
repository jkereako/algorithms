import algorithms
from algorithms import breadth_first_search
import unittest

class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.adjacency_list = { 'A': ['B', 'C'],
                                'B': ['C', 'D'],
                                'C': ['D'],
                                'D': ['C'],
                                'E': ['F'],
                                'F': ['C']}

    def test_connected_components(self):
        expected = ['E', 'F', 'C', 'D']
        self.assertTrue(
            breadth_first_search.connected_components(self.adjacency_list, 'E') == expected
        )

from algorithms import heap_sort
import heapq
import unittest

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.list = [9, 21, 3, 19, 290, 39, 343, 1 , 4, 6, 64, 3, 2, 13]
        self.expected = [1, 2, 3, 3, 4, 6, 9, 13, 19, 21, 39, 64, 290, 343]

    def test_sort(self):
        thing = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
        heapq.heapify(thing)
        print(thing)
        result = heap_sort.sort([1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2])
        self.assertTrue(result == self.expected)

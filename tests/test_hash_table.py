import data_structures
from data_structures import hash_table
import unittest

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hashTable = hash_table.HashTable(4)

    def tearDown(self):
        self.hashTable = None

    def test_create_table(self):
        self.assertTrue(self.hashTable.table  == [[], [], [], []])

    def test_remainder_method(self):
        self.assertTrue(self.hashTable.remainder_method(30) == 2)

    def test_mid_square_method(self):
        self.assertTrue(self.hashTable.mid_square_method(55) == 2)

    def test_hash_string(self):
        self.assertTrue(self.hashTable.hash_string('abc') == 2)

    def test_insert_with_linear_addressing(self):
        self.hashTable .insert('abc')
        self.assertTrue(self.hashTable.table[2] == ['abc'])


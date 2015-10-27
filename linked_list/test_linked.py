from linked_list import Node, LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        l_list = LinkedList()
        l_list.insert("David")
        self.assertTrue(l_list.head.get_data() == "David")
        self.assertTrue(l_list.head.get_next() is None)


    def test_insert_two(self):
        l_list = LinkedList()
        l_list.insert("David")
        l_list.insert("Thomas")
        self.assertTrue(l_list.head.get_data() == "Thomas")
        head_next = l_list.head.get_next()
        self.assertTrue(head_next.get_data() == "David")


    def test_nextNode(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")
        self.assertTrue(l_list.head.get_data() == "Rasmus")
        head_next = l_list.head.get_next()
        self.assertTrue(head_next.get_data() == "Pallymay")
        last = head_next.get_next()
        self.assertTrue(last.get_data() == "Jacob")


    def test_positive_search(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")
        found = l_list.search("Jacob")
        self.assertTrue(found.get_data() == "Jacob")
        found = l_list.search("Pallymay")
        self.assertTrue(found.get_data() == "Pallymay")
        found = l_list.search("Jacob")
        self.assertTrue(found.get_data() == "Jacob")


    def test_searchNone(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        # make sure reg search works
        found = l_list.search("Jacob")
        self.assertTrue(found.get_data() == "Jacob")
        # with pytest.raises(ValueError):
        #     l_list.search("Vincent")


    def test_delete(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")
        l_list.delete("Rasmus")
        self.assertTrue(l_list.head.get_data() == "Pallymay")
        l_list.delete("Jacob")
        self.assertTrue(l_list.head.get_next() is None)


    def test_delete_value_not_in_list(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")

        with self.assertRaises(ValueError):
            l_list.delete("Sunny")


    def test_delete_empty_list(self):
        l_list = LinkedList()

        with self.assertRaises(ValueError):
            l_list.delete("Sunny")
            
    def test_delete_next_reassignment(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Cid")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")
        l_list.delete("Pallymay")
        l_list.delete("Cid")
        self.assertTrue(l_list.head.next_node.get_data() == "Jacob")

if __name__ == '__main__':
    unittest.main()

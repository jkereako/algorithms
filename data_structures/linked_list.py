class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

        return new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head

        while current:
            if current.get_data() == data:
                break

            current = current.get_next()

        if not current:
            raise ValueError("Data not in list")

        return current

    def delete(self, data):
        current = self.head
        previous = None

        while current:
            if current.get_data() == data:
                break

            previous = current
            current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")

        # `previous` is `None` if the head of the list is the node we're looking
        # for.
        if previous is None:
            self.head = current.get_next()

        else:
            previous.set_next(current.get_next())

    def middle(self):
        tortoise = self.head
        hare = self.head

        while hare and hare.get_next():
            hare = hare.get_next().get_next()
            tortoise = tortoise.get_next()

        return tortoise

    def has_cycle(self):
        tortoise = self.head
        hare = self.head

        # Advance the list 
        while tortoise and hare and hare.get_next():
            hare = hare.get_next().get_next()
            tortoise = tortoise.get_next()

            if tortoise == hare:
                return True

        return False

    def delete_duplicates(self):
        """
        In order to properly delete duplicates from a linked list, you must
        advance the list in normal fashion and then compare the current node
        with all previous nodes.
        """
        current = self.head
        previous = None

        while current:
            runner = self.head
            # Iterate from the front of the list to the current pointer
            while runner and runner != current:
                if current.get_data() == runner.get_data():
                    previous.set_next(current.get_next())
                    current = previous
                    break

                runner = runner.get_next()

            previous = current
            current = current.get_next()

    def reverse(self):
        """
        Reverses a string without a stack. The running time of this algorithm is
        O(n) because we're iterating from the head to the middle and the middle
        to the tail.
        """
        middle = self.middle()
        size = self.size()
        middle_index = size // 2
        current = self.head

        # Iterate from the head to the middle of the list
        i = 0
        while i != middle_index and current:
            # On the first iteration, `k` is the index of the tail. Then, on the
            # next iteration, `k` is the index of the tail - 1 and so on.
            k = ((size - middle_index) - i) - 1
            j = 0

            # Always reset the tail to the middle node
            tail = middle

            # Iterate from the middle to the tail of the list
            while j < k and tail:
                tail = tail.get_next()
                j += 1

            # Swap the data only, it isn't necessary to swap the pointers.
            temp = current.data
            current.data = tail.data
            tail.data = temp

            current = current.get_next()
            i += 1

    def __str__(self):
        current = self.head
        string = ''
        while current:
            string += str(current) + '-->'
            current = current.get_next()

        return string

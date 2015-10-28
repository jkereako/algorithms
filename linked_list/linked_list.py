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
        tortoise = None
        hare = None

        while tortoise and hare and hare.get_next():
            hare = tortoise.get_next().get_next()
            tortoise = tortoise.get_next()
        
        return tortoise


    def has_cycle(self):
        tortoise = None
        hare = None

        # Advance the list 
        while tortoise and hare and hare.get_next():
            hare = tortoise.get_next().get_next()
            tortoise = tortoise.get_next()

            if tortoise == hare:
                return True

        return False
    
    def __str__(self):
        current = self.head
        string = ''
        while current:
            string += str(current) + '-->'
            current = current.get_next()

        return string

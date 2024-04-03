class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def remove_tail(self):
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev


    def insert_after(self, data, new_data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current == self.tail:
                    self.insert_tail(new_data)
                else:
                    new_node = Node(new_data)
                    new_node.prev = current
                    new_node.next = current.next
                    current.next.prev = new_node
                    current.next = new_node
                return    
            current = current.next

    def remove(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current == self.head:
                    self.remove_head()
                elif current == self.tail:
                    self.remove_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def replace(self, data, new_data):
        current = self.head
        while current is not None:
            if current.data == data:
                current.data = new_data
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=', ')
            current = current.next
        print()
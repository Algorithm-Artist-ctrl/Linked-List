class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print("None")
ll = LinkedList()
ll.insert_at_beginning(2)
ll.insert_at_beginning(5)
ll.insert_at_beginning(10)

ll.print_list()

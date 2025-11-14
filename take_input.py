class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def Print_LL(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next

def take_input():
    head = None
    tail = None
    
    value = int(input("Enter value of NewNode (-1 to stop): "))
    while value != -1:
        newNode = Node(value)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode   

        value = int(input("Enter value of NewNode (-1 to stop): "))
    
    return head

newhead = take_input()
Print_LL(newhead)

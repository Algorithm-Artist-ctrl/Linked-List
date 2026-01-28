class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates_sorted(head):
    curr = head

    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head

a = Node(1)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(3)
f = Node(4)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
head = remove_duplicates_sorted(a)
curr = head
while curr:
    print(curr.data, end=" → ")
    curr = curr.next

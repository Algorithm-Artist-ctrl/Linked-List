class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_kth(head, k):
    if head is None:
        return None
    if k == 0:
        return head.next

    curr = head
    for _ in range(k - 1):
        if curr.next is None:
            return head
        curr = curr.next

    if curr.next is not None:
        curr.next = curr.next.next

    return head
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
a = delete_kth(a, 2)
curr = a
while curr:
    print(curr.data, end=" → ")
    curr = curr.next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def is_palindrome(head):
    if head is None or head.next is None:
        return True
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    curr = slow

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    left = head
    right = prev

    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next

    return True
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(2)
e = Node(1)
a.next = b
b.next = c
c.next = d
d.next = e
print(is_palindrome(a))  

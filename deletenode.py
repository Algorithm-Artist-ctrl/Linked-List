class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
node_to_delete = head.next
Solution().deleteNode(node_to_delete)
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

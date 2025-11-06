class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        curr = head
        l = 0
        while curr != None:
            curr = curr.next
            l += 1
        curr = head
        for i in range(l // 2):
            curr = curr.next
        return curr 
head = ListNode(1, ListNode(2, ListNode(3)))
Sol = Solution()
mid = Sol.middleNode(head)
print(mid.val)  

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
first=Node(1)
Second=Node(2)
Third=Node(3)
first.next=Second
#Second.next=Third
first.next.next=Third
head=first
print(first.next.data)
print(first.next.next.data)

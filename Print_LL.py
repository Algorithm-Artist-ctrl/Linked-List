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
def Print_LL(head):
    temp=head # once your head lost there is no way to recover it hence store in anothere variable for backup
    while(temp!=None):
        print(temp.data)
        temp=temp.next 
    return
print(Print_LL(head))

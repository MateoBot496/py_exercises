class linkedList:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

node4= linkedList(4)
head= linkedList(1,linkedList(2,linkedList(3,node4))) #12 24
node4.next=head

#SABER SI UNA LINKED LIST TIENE UN BUCLE

def isCyclic(head: linkedList) -> bool:
    slow = fast = head
    fast = fast.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

print(isCyclic(head))
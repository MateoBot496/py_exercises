class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Valor del nodo
        self.next = next  # Puntero al siguiente nodo

head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1
                                                                )))))

def findMid(head: ListNode):
    ptr1 = ptr2 = head

    while ptr2 and ptr2.next:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next

    return ptr1
    

def reversedList(head: ListNode) -> ListNode:   
    current = head
    prev = None

    while current:
        temp = current.next  # Guarda el siguiente nodo
        current.next = prev  # Invierte el enlace
        prev = current       # Mueve prev hacia adelante
        current = temp       # Mueve current hacia adelante

    return prev  # El nuevo head de la lista invertida

    
    

def palindrome(head: ListNode) -> bool:
    mid = findMid(head)
    reversed = reversedList(mid)

    while reversed:
        if head.val != reversed.val:
            return False
        head,reversed = head.next, reversed.next

    
    return True





print(palindrome(head))

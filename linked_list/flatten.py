class linkedList:
    def __init__(self, val=0, next=None, child=None):
        self.child=None
        self.next=None
        self.value=val
head = linkedList(1)
node2 = linkedList(2)
node3 = linkedList(3)
node4 = linkedList(4)
node5 = linkedList(5)

# Enlazar la lista principal
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Crear nodos del nivel 1 (hijos de la lista principal)
node6 = linkedList(6)
node7 = linkedList(7)

# Enlazar nodos en el nivel 1
node6.next = node7  # 6 -> 7

# Crear nodos del nivel 2 (hijos del nivel 1)
node8 = linkedList(8)
node9 = linkedList(9)

# Enlazar nodos en el nivel 2
node8.next = node9  # 8 -> 9

# Crear nodo del nivel 3 (hijo del nivel 2)
node10 = linkedList(10)

# Conectar niveles
node2.child = node6  # 2 -> 6
node3.child = node8  # 3 -> 8
node6.child = node10  # 6 -> 10


#FLATTEN

def flatten(head: linkedList):
    curr = tail = head #CREAMOS 2 POINTERS CURR Y TAIL
    
    while tail.next: 
        tail=tail.next #ponemos TAIL AL FINAL
    
    while curr:
        if curr.child:
            tail.next=curr.child
            curr.child=None
            while tail.next:
                tail = tail.next
        curr=curr.next
            
    return head
 
flatten(head)
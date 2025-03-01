queue = []
queue2 = []

def enqueue(number: int):
    queue.append(number)
    return

def dequeue():
    if not queue2:
        while queue:
            queue2.append(queue.pop())
    
    if queue2:
        return queue2.pop()
    
    return None

def peek():

    if not queue2:
        while queue:
            queue2.append(queue.pop())
    
    if queue2:
        return queue2[-1]
    
    return None


enqueue(1)
enqueue(2)
dequeue()
peek()
enqueue(3)
print(queue)

#SE USAN 2 STACKS QUEUE Y DEQUEUE PORQUE SOLO 1 SERIA INEFICIENTE DE TIEMPO YA QUE POP(0) MUEVE TODOS LOS ELEMENTOS Y SERIA O(N)
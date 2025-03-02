from collections import deque

def maxSlidingWindow(arr: list[int], k: int) -> list[int]:
        resultado = []
        dq = deque()

        for i, num in enumerate(arr):
            while dq and num > dq[-1]:
                dq.pop()
            dq.append(num)

            if i >= k and arr[i - k] == dq[0]: #si el numero mas antiguo de la ventana esta en nuestro arr
                dq.popleft()

            if i >= k-1:
                resultado.append(dq[0])
            
        return resultado

arr = [3,2,4,1,2,1,1]

print(maxSlidingWindow(arr,4))

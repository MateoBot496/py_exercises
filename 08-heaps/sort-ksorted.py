import heapq


def ksort(arr: list[int],k):
    min_heap = arr[:k+1] #creamos un heap minimo
    heapq.heapify(min_heap)

    index = 0

    for i in range(k+1 , len(arr)):
        arr[index]= heapq.heappop(min_heap) #quitamos con heappop el index 0 el mas bajko, y lo metemos en arr index0
        index+=1
        heapq.heappush(min_heap, arr[i])

    while min_heap:
        arr[index]= heapq.heappop(min_heap)
        index+=1


    return arr

arr = [5,1,9,4,7,10]
print(ksort(arr,2))
def inMatrix(matrix, target:int) -> bool:
    rows = len(matrix)
    columns = len(matrix[0])

    #CREAMOS 2 POINTERS PARA HACER BINARY SEARCH
    totalLen = rows * columns
    lptr = 0
    rptr = totalLen -1
    

    #SABEMOS QUE LA POSICION XY DEL PUNTO MID ES MID(6), // COLUMNS(4)(RES 1), E Y ES MID // ROWS(3)(RES2) XY = 1,2
    


    
    while lptr <= rptr:
        mid = (lptr + rptr)//2
        x = mid // columns
        y = mid % columns

        if target == matrix[x][y]:
            return True
        elif target > matrix[x][y]:
            lptr = mid+1

        elif target < matrix[x][y]:
            rptr = mid-1

    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
targetb = 400
print(inMatrix(matrix, target))
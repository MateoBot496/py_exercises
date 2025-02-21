def isHappy(num: int, visited = set()) -> bool:

    

    if num==1:
        return True
    
    if num in visited:
        return False
    
    visited.add(num)

    numeros = list(str(num)) #lo metemos en un array
    temp = 0

    for i in range(len(numeros)): #SUMAMOS LOS CUADRADOS DE NUMEROS Y LOS GUARDAMOS EN TEMP
        temp += int(numeros[i]) * int(numeros[i])

    
    return isHappy(temp, visited)
    





print(isHappy(9))  
def longestChain(nums: list[int]): #ENCONTRAMOS LA CADENA DE NUMEROS CONSECUTIVOS MAS LARGA, LO HACEMOS CON HASHSET YA QUE ES LA FORMA MAS EFICIENTE EN TIEMPO Y ESPACIO. ORDENAR Y OTROS METODOS SON PEORES
    if not nums:
        print("Debe introducir etc...")

    nums_set=set(nums) #metemos en un set
    longest_Chain=0
    

    for num in nums_set: #por cada numero en el set
        current_chain=0
        if num -1 not in nums_set: #si no hay un numero menor en el set
            this_num=num
            current_chain+=1
            while this_num +1 in nums_set: #mientras haya un numero mayor en el set
                current_chain+=1
                this_num+=1
        if current_chain > longest_Chain:
            longest_Chain = current_chain    
    
    return longest_Chain


numeros = [3,2,1,6,5,7,8,15,13,14,16,17]
print(longestChain(numeros))
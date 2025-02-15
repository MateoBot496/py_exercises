def shift(nums: list[int]): #ESTA FUNCION ES UN POCO ARCAICA, NAIVE TIME COMPLEXITY O(N) SPACE O(2)
    temp = []
    ceros = 0
    for numero in nums:
        if numero != 0:
            temp.append(numero)
        else:
            ceros+=1

    for i in range(ceros):
        temp.append(0)
        
    return temp


numeros = [0 , 0, 0 , 3 , 5 , 0 , 2 , 0 , 0 , 223 , 6 , 0 ,23458585]





#VAMOS A MEJORARLA EL TIEMPO SERA IGUAL PERO EL ESPACIO SERA 1 //Y LA INTENTAMOS HACER RECURSIVA

def shiftPro(nums: list[int], left=0, right=1):

    if right == len(nums):
            return
    
    if nums[left]==0 and nums[right]==0:
        right+=1
    
    elif nums[left]==0 and nums[right]!=0:
        nums[left], nums[right] = nums[right], nums[left]
        left +=1
        right +=1
        
    else:
        left +=1
        right +=1

    shiftPro(nums, left, right)

    
shiftPro(numeros)
print(numeros)
numeros = [0 , 0, 0 , 3 , 5 , 0 , 2 , 0 , 0 , 223 , 6 , 0 ,23458585]


# OTRA OPCION DONDE RETURN NUMS

def shiftPro(nums: list[int], left=0, right=1):

    if right == len(nums):
            return nums
    
    if nums[left]==0 and nums[right]==0:
        return shiftPro(nums, left, right+1)
    
    elif nums[left]==0 and nums[right]!=0:
        nums[left], nums[right] = nums[right], nums[left]
        return shiftPro(nums, left+1, right+1)
        
    else:
        return shiftPro(nums, left+1, right+1)


    

print(shiftPro(numeros))

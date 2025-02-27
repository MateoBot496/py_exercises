def localMaxima(nums: list[int]):

    lptr = 0
    rptr = len(nums)-1
    

    while lptr <= rptr: #OPTIMIZACION 1 QUITAR EL IGUAL EN CASO DE QUE FUERAN IGUALES, SE DEVUELVE LEFT
        mid = (lptr+rptr)//2



        #COMPROBAMOS SI MID ES MAXIMO O MINIMO PARA NO COMPARARLO CON -1 O FUERA DE ARRAY
        if mid == 0:
            if nums[mid] > nums[mid+1]:
                return mid
            
        elif mid == len(nums)-1 :
            if nums[mid] > nums[mid-1]:
                return mid
            
        elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        
        #SI NINGUNA DE LAS ANTERIORES HACE RETURN, VENIMOS AQUI Y CAMBIAMOS LOS PTRS
        
        if mid == 0:
            lptr=mid+1
            continue
        if mid == len(nums)-1:
            rptr = mid-1
            continue

        if nums[mid-1]>nums[mid]:
            rptr = mid-1
            continue
        if nums[mid+1]>nums[mid]:
            lptr = mid+1


    return False      


def local_maxima_in_array(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
    


nums = [1,2]
print(local_maxima_in_array(nums))
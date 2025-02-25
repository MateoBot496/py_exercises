import math

def median(nums1:list[int], nums2:list[int]):
    if len(nums1) > len(nums2):
        nums1,nums2=nums2,nums1
    
    halfTotalLen = math.floor(      (len(nums1) + len(nums2))/2     )
    left = 0
    right = len(nums1)-1 #FINAL DEL ARRAY

    indexl1 = (left + right) // 2 #buscamos la mitad de nums 1
    
    

    while True:

        indexl2 = halfTotalLen - indexl1    #TIENE QUE HABER HALF TOTAL LEN EN CADA MITAD, 
        
        L1 = float('-inf') if indexl1 <= 0 else nums1[indexl1 -1]
        R1 = float('inf') if indexl1 >= len(nums1) else nums1[indexl1]

        L2 = float('-inf') if indexl2 <= 0 else nums2[indexl2-1]
        R2 = float('inf') if indexl2 >= len(nums2) else nums2[indexl2]



        if L1>R2:
            indexl1-=1
        
        elif L2 > R1:
            indexl1+=1

        else:
            if (len(nums1) + len(nums2)) %2 == 0 :
                return (max(L1, L2) + min(R1, R2)) / 2.0
            
            else:
                return min(R1,R2)

nums1 = [1,2,3,88,526]
nums2 = [4,5,6,23]

print(median(nums1,nums2))
import random
class Solution:

    def __init__(self, w: list[int]):
        self.nums = w
        self.totalSum=[self.nums[0]]
        for i in range(1,len(self.nums)):
            self.totalSum.append(self.totalSum[i-1]+self.nums[i])
    
    def pickIndex(self):
        peso = self.totalSum[ len(self.totalSum)-1 ]
        rng = random.randint(1, peso) #NUMERO RANDOM DE 1 A TOTAL DE PESO [135] PESO 9, SACA NUMERO RANDOM

        lptr = 0
        rptr = len(self.nums)-1

        while lptr < rptr:

            mid = (lptr+rptr)//2

            if self.totalSum[mid] < rng:
                lptr = mid+1
            else:
                rptr = mid

        return lptr



        

#3,17,18,25
nums =[3,14,1,7]

solucion = Solution(nums)
print(solucion.pickIndex())
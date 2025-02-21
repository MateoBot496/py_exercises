
from collections import defaultdict
def triplets(nums: list[int], r):
    
    leftMap = defaultdict(int)
    rightMap = defaultdict(int)
    count = 0

    for num in nums:
        rightMap[num]+=1

    for num in nums:
        rightMap[num]-=1
        if num % r == 0:
            count += leftMap[num / r] * rightMap [num * r]
        leftMap[num]+=1

    return count

nums = [2,1,2,4,8,8]
r = 2

print(triplets(nums, r))
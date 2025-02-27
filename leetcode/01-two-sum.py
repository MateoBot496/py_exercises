
def twoSum(nums: list[int], target: int) -> list[int]:
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return [] 
            
nums = [3,2,2]

target = 9

print(twoSum(nums, target))
# 1) Two Sum
#Topic: Arrays
## brute force
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(1+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

## Optimized
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
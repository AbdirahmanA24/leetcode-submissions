# 217) Contains Duplicates
# Topics: Arrays, Sorting
def containsDuplicates(nums):
    seen = set()
# cannot initialize a empty set using = {}
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
#we are given an array of numbers and a target number, if two numbers in the array add up to the target number, return the indices of the two numbers

def twoSum(nums, target):
    hashset = {}
    for i in range(len(nums)):
        check = target - nums[i]
        if check in hashset:
            return [hashset[check], i]
        hashset[nums[i]] = i
    return []

#test cases
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
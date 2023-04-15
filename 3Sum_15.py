#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# use enumerate to get index and value
def threeSum(nums):
    nums.sort()
    result = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum < 0:
                l += 1
            elif threeSum > 0:
                r -= 1
            else:
                result.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
    return result

#3 test case
nums = [0, 0, 0, 0]
print(threeSum(nums))
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
nums = [-2, 0, 1, 1, 2]
print(threeSum(nums))

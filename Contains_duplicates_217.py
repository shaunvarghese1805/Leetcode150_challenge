#If array nums contains atleat one pair of duplicates, return true. Else return False 


def containsDuplicate(nums):
    hashset = set()
    
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(containsDuplicate([1,2,3,4,1]))
print(containsDuplicate([2,3,4,1]))
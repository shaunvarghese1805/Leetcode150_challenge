#If array nums contains atleat one pair of duplicates, return true. Else return False 


def containsDuplicate(nums):
    #here we use set to check if the element is already present in the input
    hashset = set()
    
    for n in nums:
        #if the element is already present in the set then return true
        if n in hashset:
            return True
        hashset.add(n)
    #returns false after going through the entire array and exiting the loop
    return False

print(containsDuplicate([1,2,3,4,1]))
print(containsDuplicate([2,3,4,1]))
#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#remove comments 
def productExceptSelf(nums):
    #create a list of 1's of the same length as nums
    res = [1] * len(nums)
    #create a variable pre and assign it to 1
    pre = 1
    #loop through the nums list
    for i in range(len(nums)):
        #assign the value of pre to res[i]
        res[i] = pre
        #multiply pre by nums[i]
        pre *= nums[i]
    #create a variable pos and assign it to 1
    pos = 1
    #loop through the nums list in reverse
    for i in range(len(nums)- 1, -1, -1):
        #multiply res[i] by pos
        res[i] *= pos
        #multiply pos by nums[i]
        pos *= nums[i]
        
    return res
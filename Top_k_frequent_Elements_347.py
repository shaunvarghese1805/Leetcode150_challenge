#Given an integer array nums and an integer k, return the k most frequent elements.

#def getvalue(item):
#    return item[1]
from collections import defaultdict
def topkfreq(nums, k):
    check = defaultdict(int)

    for n in nums:
        check[n] += 1
    #here we are sorting the dictionary based on the values
    #lamda function is used to sort the dictionary based on the values
    # instead of lambda we can use a function to do the same
    #sorted_check = sorted(check.items(), key = getvalue, reverse= True) for this uncomment the above function
    sorted_check = sorted(check.items(), key = lambda x:x[1], reverse= True)

    result = []

    for i in range(k):
        result.append(sorted_check[i][0])
    
    return result
#test cases
print(topkfreq([1,1,1,2,2,3], 2))
print(topkfreq([1], 1))
print(topkfreq([1,2], 2))
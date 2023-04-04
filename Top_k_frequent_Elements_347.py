#Given an integer array nums and an integer k, return the k most frequent elements.

from collections import defaultdict
def topkfreq(nums, k):
    check = defaultdict(int)

    for n in nums:
        check[n] += 1
    
    sorted_check = sorted(check.items(), key = lambda x:x[1], reverse= True)

    result = []

    for i in range(k):
        result.append(sorted_check[i][0])
    
    return result

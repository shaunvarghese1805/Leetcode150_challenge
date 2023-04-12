#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.

def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while r > l:
        cursum= numbers[l] + numbers[r]

        if cursum> target:
            r-=1
        elif cursum< target:
            l+= 1
        else:
            return [l + 1, r + 1]
        

   
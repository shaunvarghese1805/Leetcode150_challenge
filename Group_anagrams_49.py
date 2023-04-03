#given a array of strings, group anagrams together

from collections import defaultdict
def groupAnagrams(strs):
    hashset = defaultdict(list)
    result = []
    for s in strs:
        s_sorted = tuple(sorted(s))
        hashset[s_sorted].append(s)

    for value in hashset.values():
        result.append(value)
    return result

#test cases
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
print(groupAnagrams(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]))

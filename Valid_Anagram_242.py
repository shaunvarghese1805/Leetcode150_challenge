# Given two strings "s" and "t", if they are anagrams then return true, else return false.

def anagramchecker(t ,s):
    if len(s)!= len(t):
        return False
    if sorted(s)==sorted(t):
        return True
    else:
        return False

print(anagramchecker(t = "plenty",s = "yplent"))
print(anagramchecker(t = "car",s = "tar"))
print(anagramchecker(t = "Camera",s = "Hour"))
print(anagramchecker(t = "cars",s = "car"))
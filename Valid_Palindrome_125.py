#Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    newstr = ""

    for n in s:
        if n.isalnum():
            newstr+= n.lower()

        inv_newstr = newstr[::-1]
        return newstr == inv_newstr
           
#Test cases
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

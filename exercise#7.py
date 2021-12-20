# Write a recursive function called isPalindrome which returns true if the string passed to it
# is a palindrome (reads the same forward and backward). Otherwise it returns false.


def isPalindrome(strng):
    if strng[::-1] == strng:
        return True
    else:
        return False


print(isPalindrome('cat'))
print(isPalindrome('kek'))
print(isPalindrome('tacocat'))

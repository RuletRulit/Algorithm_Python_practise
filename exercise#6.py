# Write a recursive function called reverse
# which accepts a string and returns a new string in reverse.


def reverse(strng):
    if strng == "":
        return strng
    else:
        return strng[-1] + reverse(strng[:-1])


print(reverse('dima'))



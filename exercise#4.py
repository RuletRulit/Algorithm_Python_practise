# Write a function called recursiveRange which accepts a number and adds up all the numbers from
# 0 to the number passed to the function.


def recursiveRange(num):
    assert int(num) == num and int(num) > 0, 'Must be a positive integer'
    if num == 1:
        return 1
    return recursiveRange(num - 1) + num


print(recursiveRange(300))

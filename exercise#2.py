# Write a function factorial which accepts a number and returns the factorial of that number.
# A factorial is the product of an integer and
# all the integers below it; e.g., factorial four ( 4! ) is equal to 24, because 4 * 3 * 2 * 1 equals 24.
# factorial zero (0!) is always 1


def factorial(num):
    assert int(num) == num, 'Must be an integer'
    if num == 0:
        return 1
    elif num > 0:
        return factorial(num - 1) * num


print(factorial(-5))

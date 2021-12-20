# Write a recursive function called fib which accepts a number and returns the nth
# number in the Fibonacci sequence. Recall that the Fibonacci sequence
# is the sequence of whole numbers 0,1, 1, 2, 3, 5, 8, ... which starts with 0 and 1,
# and where every number thereafter is equal to the sum of the previous two numbers.


def fib(num):
    if num <= 2:
        return 1
    elif num == 0:
        return 1
    else:
        return fib(num - 2) + fib(num - 1)


print(fib(4))

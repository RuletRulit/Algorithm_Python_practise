# Write a recursive function called flatten which accepts an array of arrays
# and returns a new array with all values flattened.


def flatten(arr):
    if isinstance(arr, list):
        if len(arr) == 0:
            return []
        first, rest = arr[0], arr[1:]
        return flatten(first) + flatten(rest)
    else:
        return [arr]


print(flatten([1, 2, [2, 5, [7]]]))

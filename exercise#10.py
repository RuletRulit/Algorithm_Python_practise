# Write a recursive function called capitalizeFirst.
# Given an array of strings, capitalize the first letter of each string in the array.


def capitalizeFirst(arr):
    first, rest = arr[0].capitalize(), arr[1:]
    if len(arr) > 1:
        return [first] + capitalizeFirst(rest)
    return [first]


print(capitalizeFirst(['car', 'taco', 'banana', 'deliver']))

# Write a recursive function called nestedEvenSum.
# Return the sum of all even numbers in an object which may contain nested objects.

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}


def nestedEvenSum(obj):
    for key, value in obj.items():
        if type(obj) is dict:
            print(key, value)
            return nestedEvenSum({key: value})
        else:
            print(value)





    # for key, value in _obj.items():
    #     if isinstance(value, dict):
    #         print(value, "ce dict")
    #         return nestedEvenSum(value, sum)
    #     else:
    #         if value % 2 == 0:
    #             print(value, "ce int")
    #             sum += value



#
# def iterdict(d):
#   for k,v in d.items():
#      if isinstance(v, dict):
#          iterdict(v)
#      elif isinstance(v, int) and v % 2 == 0:
#         print(v)



# print(iterdict(obj1))


# print(nestedEvenSum(obj1, sum=0))
print(nestedEvenSum(obj2))
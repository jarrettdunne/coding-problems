from pprint import pprint
import inspect
import re

def complexity(func):
    print(inspect.getsource(func))
    return func

@complexity
def two_sum(lst:list, k:int):
    '''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    '''
    # For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    result = two_sum([10, 15, 3, 7], 17)

    # print(result)
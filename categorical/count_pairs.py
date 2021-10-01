# Given an integer array and a number k.
# Count all pairs where:
# a + k = b || a - b == k

def count_pairs(numbers, k):
    ''''''
    c = get_combinations(numbers, 2)
    valid_pairs = list(filter(lambda v: v[0] + k == v[1], c))
    return len(valid_pairs)

def factorial(n):
    ''''''
    accum = 1
    for i in range(1, n):
        accum *= i
    return accum

def combinations(n, k):
    ''''''
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

def get_combinations(array, tuple_length, prev_array=[]):
    ''''''
    if len(prev_array) == tuple_length:
        return [prev_array]

    combs = []
    for i, val in enumerate(array):
        prev_array_extended = prev_array.copy()
        prev_array_extended.append(val)
        combs += get_combinations(array[i+1:], tuple_length, prev_array_extended)
    
    return combs

if __name__ == "__main__":
    ''''''
    array = [1, 1, 2, 3, 3, 5]
    print(count_pairs(array, 3))
def sum_product(array):
    s = 1
    for i in array:
        s *= i
    return s

def array_product(array):
    s = sum_product(array)
    return [int(s / i) for i in array]

array = [1, 2, 3, 4, 5]

print(array_product(array))

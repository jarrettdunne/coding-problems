'''
This problem was asked by Google.

Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.
'''

A = [[1, 3, 7, 10, 15, 20],
     [2, 6, 9, 14, 22, 25],
     [3, 8, 10, 15, 25, 30],
     [10, 11, 12, 23, 30, 35],
     [20, 25, 30, 35, 40, 45]]

def func(A, i1, j1, i2, j2):
    a = A[i1][j1]
    b = A[i2][j2]
    n = len(A)
    m = len(A[0])
    count  = 0
    for i in range(n):
        for j in range(m):
          # print(A[i][j])
          if A[i][j] < a or A[i][j] > b:
               count += 1
    return count
                

res = func(A, 1, 1, 3, 3)
print(res)

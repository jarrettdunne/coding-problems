def sum_two_from_list(ls, k):
    for i in ls:
        for j in ls:
            if sum([i, j]) == k:
                print([i, j])
                return True

ls = [3, 14, 5, 7, 2, 8, 1, 10]
k = 12

sum_two_from_list(ls, k)

# Given a number in the form of a list of digits, return all possible permutations.

# For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

def factorial(n):
    for i in list(range(1, n + 1)):
        print(i)
    return 

def list_permutations(ls):
    n = len(ls)
    # P = n! / (n - r)!
    # P = n! / 1

    return

def permu(nums):
    if (len(nums) == 1):
        return [nums]

    output = []
    for l in permu(nums[1:]):
        for i in range(len(nums)):
            # print(l[:i])
            # print([nums[0]])
            # print(l[:i])
            # print(l[:i] + [nums[0]] + l[i:])
            output.append(l[:i] + [nums[0]] + l[i:])
            print(output)
    
    return output
    return output

if __name__ == "__main__":
    ls = [1, 2, 3]
    p = permu([1,2, 3])

    print(p)
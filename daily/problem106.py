# This problem was asked by Pinterest.

# Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

# For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

def hops(ls:list):
    last_index = len(ls)
    # hops moves
    # hops stays
    #   moves 0 or is at end

if __name__ == "__main__":
    list1 = [2, 0, 1, 0]
    list2 = [1, 1, 0, 1]
    list3 = [2, 0, 2, 2]

    print(hops(list1))
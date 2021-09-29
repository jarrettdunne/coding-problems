# Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.
# 
# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.

def smallest_set_of_intervals(intervals):
    ''''''
    # Assumptions:
    #   intervals can overlap eachother
    #   

    # separate sets into two lists of lower limits and upper limits
    # then take the lowest upper limit and highest lower limit
    lowers = []
    uppers = []

    for s in intervals:
        lowers.append(s[0])
        uppers.append(s[1])
    
    return set([lowers[len(lowers) - 1], uppers[0]])

if __name__ == "__main__":
    ''''''
    print(smallest_set_of_intervals([[0, 3], [2, 6], [3, 4], [6, 9]]))
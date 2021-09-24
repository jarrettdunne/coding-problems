# Problem 91

# What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

def problem91():
    functions = []
    for i in range(10):
        print(i)
        functions.append(lambda : i)

    for f in functions:
        print(f())

if __name__ == "__main__":
    problem91()
    x = lambda : 1
    print(x())
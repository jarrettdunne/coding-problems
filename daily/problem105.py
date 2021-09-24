# This problem was asked by Facebook.

# Given a function f, and N return a debounced f of N milliseconds.

# That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.

import asyncio
import time

def debounce(func, N=1000):
    if state:
        time(N)
    return func

@debounce
def switch():
    return

if __name__ == "__main__":
    debounce()
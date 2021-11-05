
fib_cache = {}

def fib(n):
    if n < 0:
        raise Exception("Invalid number!")

    if n < 2:
        fib_cache[n] = n
        return n

    if n in fib_cache:
        return fib_cache[n]

    fib_cache[n] = fib(n - 1) + fib(n - 2)
    return fib_cache[n]

x = 0
print(fib(x))
print(fib_cache)

for i in range(x):
    print(fib_cache[i])

"""
fib(5)
-- fib(4)
---- fib(3)
------ fib(2)
--------- fib(1)


fib(0): 0
fib(1): 1
fib(2): 1
fib(3): 2
fib(4): 3
fib(5): 5
"""

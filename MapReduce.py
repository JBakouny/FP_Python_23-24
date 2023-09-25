from functools import partial
# def multiply(x, y, z):
#     return x * y * z
#
# # create a new function that multiplies by 2
# fp = partial(multiply, 2, 3)
# print(fp(4))

def sum(f, a, b):
    if a > b:
        return 0
    else:
        return f(a) + sum(f, a + 1, b)

def product(f, a, b):
    if a > b:
        return 1
    else:
        return f(a) * product(f, a + 1, b)


sumInts = partial(sum, lambda x: x)
sumCubes = partial(sum, lambda x: x ** 3)

def fact(n) :
    return product(lambda x : x, 1, n)

sumFact = partial(sum, fact)

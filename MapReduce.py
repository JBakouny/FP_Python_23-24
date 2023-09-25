from functools import partial
# def multiply(x, y, z):
#     return x * y * z
#
# # create a new function that multiplies by 2
# fp = partial(multiply, 2, 3)
# print(fp(4))


def mapReduce(zero, op, f, a, b):
    if a > b:
        return zero
    else:
        return op(f(a), mapReduce(zero, op, f, a + 1, b))

sum = partial(mapReduce, 0, lambda x, y : x + y)
product = partial(mapReduce, 1, lambda x, y : x * y)

sumInts = partial(sum, lambda x: x)
sumCubes = partial(sum, lambda x: x ** 3)

def fact(n) :
    return product(lambda x : x, 1, n)

sumFact = partial(sum, fact)

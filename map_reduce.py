from functools import partial


# def multiply(x, y, z):
#     return x * y * z
#
# # create a new function that multiplies by 2
# fp = partial(multiply, 2, 3)
# print(fp(4))


def map_reduce(zero, op, f, a, b):
    res = zero
    for i in range(a, b + 1):
        res = op(res, f(i))
    return res


sum = partial(map_reduce, 0, lambda x, y: x + y)
product = partial(map_reduce, 1, lambda x, y: x * y)

sum_ints = partial(sum, lambda x: x)
sum_cubes = partial(sum, lambda x: x ** 3)


def fact(n):
    return product(lambda x: x, 1, n)


sum_fact = partial(sum, fact)

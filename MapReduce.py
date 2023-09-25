from functools import partial


def sum(f) :
    def helper(a, b) :
        if a > b:
            return 0
        else:
            return f(a) + helper(a + 1, b)
    return helper

sumInts = sum(lambda x : x)

sumCubes = sum(lambda x : x**3)

def fact(n) :
    if n == 0 :
        return 1
    else:
        return n * fact(n-1)

sumFact = sum(fact)

print(sumCubes(0,50))
print(sumFact(0,5))
print(sumInts(0,5))
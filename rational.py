
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Rational :
    __match_args__ = ("numer", "denom")
    def __init__(self, x, y):
        g = gcd(x, y)
        self.numer = x / g
        self.denom = y / g

    def __add__(self, that):
        return Rational(self.numer * that.denom +
                 self.denom * that.numer, self.denom * that.denom)

    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)



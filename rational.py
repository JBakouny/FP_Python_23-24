from dataclasses import dataclass

@dataclass
class Rational :
    numer : int
    denom : int

    def __add__(self, that):
        return Rational(self.numer * that.denom +
                 self.denom * that.numer, self.denom * that.denom)

    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)




tolerance = 0.0000000000000000000000000001


def fixed_point(f, first_guess):
    def is_close_enough(expected, actual, precision=tolerance):
        return abs((expected - actual) / expected) < precision

    x = first_guess
    next_guess = f(x)
    while not is_close_enough(x, next_guess):
        x = next_guess
        next_guess = f(x)
    return next_guess


def average_damp(f):
    return lambda x: (x + f(x)) / 2


def sqrt(x):
    return fixed_point(average_damp(lambda y: x / y), 1)
import numpy
print("hello")


def f(x):
    if x <= 0:
        x = -x + 1
    x *= 3
    x += 2

    if x > 100:
        return True
    else:
        return False

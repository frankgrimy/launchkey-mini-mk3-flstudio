### Special math functions
import math
def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def linearize(x, x1, y1, x2, y2, n):
    m = (y2-y1)/(x2-x1)
    y = m*x+n
    return y

def linnormalize(x, x2, y2, n):
    m = y2/x2
    y = m*x+n
    return y

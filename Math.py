def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
def my_power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
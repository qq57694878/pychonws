from functools import reduce
def f(a,b):
    return a*10 +b
fi= reduce(f,[1,2,3,4,5])
print(fi)
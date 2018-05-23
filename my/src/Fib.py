class Fib(object):
    def __init__(self):
        self.a=0
        self.b=1

    def __str__(self):
        return str(self.a)

    __repr__ = __str__

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值

        return self.a  # 返回下一个值

    def __getitem__(self, n):
        a,b=1,1
        if isinstance(n,int):
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
    def __call__(self, *args, **kwargs):
        print(self)


fib = Fib()
for i in range(10):
     print(fib[i])
fib = Fib()
for i in fib:
    print(i)
    if(i>10000):
        break
print(fib[:10])
fib()
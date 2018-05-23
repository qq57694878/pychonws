import functools


def init_iter():
    n=1
    while True:
       n+=2
       yield n



def filter_iter(n):
    return lambda x: x % n > 0

def prims():
    n=2
    yield n
    iter = init_iter()
    while True:
        n=next(iter)
        yield n
        iter=filter(filter_iter(n),iter)
for i in prims():
    if i<10:
     print(i)
    else:
      break
def log(text):
    def dec(func):
        @functools.wraps(func)
        def wrap(*args,**kw):
            print('%s %s %s' % (text,func.__name__ ,'开始'))
            r = func(*args,**kw)
            print('%s %s %s' % (text, func.__name__ , '结束'))
            return r
        return wrap
    return dec

#@log('执行了')
def m1():
    print('aaa')
m1()
a = log('执行了')(m1)
print(a.__name__)

class Student(object):

  @property
  def score(self):
      return self._score
  @score.setter
  def score(self,value):
      if not isinstance(value,int):
          raise ValueError('value must be integer')
      if value < 0 or value >100:
         raise ValueError('value must be between 0-100')
      self._score =value

stu = Student()
stu.score=10
stu.score=101
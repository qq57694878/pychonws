b='1111111'
a ='A%s%d'%(b,2)
print(a)

c =1000
print(hex(c))
print(str(c))
from  Month import Month,Weekday
print(Month.Jan)
print(Weekday.Mon)

def fn(self,name):
    print('name:%s' % name)
Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello('111')
print(type(Hello))
print(type(h))
with open('f:/a/a.txt' ,'w') as f:
    f.write("你好")
    f.write("哈哈")
import os
print(os.environ.get('PATH'))
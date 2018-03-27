import os
a = os.environ.get("path")
print(a)
b = os.path.abspath(".")
print(b)
dirc = 'F:/a'




import pickle
d = dict(name='Bob', age=20, score=88)

f = open(os.path.join(dirc,'dump.txt'),'wb')
pickle.dump(d, f)
f.close()

f = open(os.path.join(dirc,'dump.txt'),'rb')
dd = pickle.load(f)
print(dd)



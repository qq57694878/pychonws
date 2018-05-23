import base64
from io import StringIO
with open('f:/a/a.txt','r') as fi:
      fo = StringIO()
      base64.encode(fi,fo)
      print(fo.getvalue())
import zipfile
import urllib
import os
import ast
from tempfile import mktemp

filename = 'p5.zip'
destDir = '.'
theurl = 'https://p5js.org/offline-reference/p5-reference.zip'
name, hdrs = urllib.urlretrieve(theurl, filename)

with zipfile.ZipFile(filename, 'r') as zf:
    zf.extract('js/data.js')

os.remove(filename)


# from
js_obj = "{'x':1, 'y':2, 'z':3}"

# to
py_obj = ast.literal_eval(js_obj)
print py_obj
for key, value in py_obj.items():
    print value

# classItems contain possible methods -> check 'itemtype'
# TODO: classes contains all the classes
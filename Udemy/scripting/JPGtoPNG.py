import sys
import pathlib

from PIL import Image

"""it's supposed to be run from terminal
example: py JPGtoPNG.py DIR_FROM DIR_TO
"""
try:
    FROM = sys.argv[1]
    TO = sys.argv[2]
except:
    print("""ERROR: should be two parameters\n
    write like this:\n
    py JPGtoPNG.py DIR_FROM DIR_TO""")

PATH = pathlib.Path.cwd()
PATH_FROM = PATH / str(FROM)
PATH_TO = PATH / str(TO)
try:
    PATH_TO.mkdir()
except:
    pass

a = PATH_FROM.iterdir()
b = [k for k in a]  # list of strings (paths)


#image processing
for item in b:
    file_name = str(item).replace(str(PATH_FROM), '')
    file_name_png = file_name[:-3] + 'png'
    img = Image.open(item)
    img.save(str(PATH_TO) + file_name_png)










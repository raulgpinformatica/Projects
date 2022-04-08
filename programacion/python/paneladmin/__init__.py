import os, re
from os import listdir

root = listdir(os.path.dirname(__file__ ) + "/clases")

classarch = []

for i in range(len(root)):
    classarch.append(re.sub('\.py$','',root[i]))

for i in range(len(classarch)):
    classarchmod = __import__("clases." + classarch[i])
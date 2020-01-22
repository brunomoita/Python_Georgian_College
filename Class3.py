import os

path = os.path.dirname(os.path.realpath('Class3.txt'))
print("Path = ", path)
fhand=open((path+'\\Class_3.txt'), 'r')
if fhand.mode == 'r':
    contents =fhand.read
    print(len(contents))
    print(contents)
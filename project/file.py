from student import *

def ReadFile(s):
    ls = []
    with open(s, 'r') as fp:
        for line in fp:
            stu = STU()
            stu.read(line.split())
            stu.cal()
            ls.append(stu)
    return ls





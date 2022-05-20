import time
class qt_class:
    def __init__(self):
        print("zero no of argument")
    def __init__(self,x1):
        print("one no of argument")
    def __init__(self,x2):
        print("two no of argument")
    def __init__(self,x3):
        print("three no of argument")
    def __init__(self,x4):
        print("four no of argument")
q1=qt_class()
print()
q1=qt_class("A")
print()
q1=qt_class("A","b")
print()
q1=qt_class("A","b","c")
print()
q1=qt_class("A","b","c","d")
print()
time.sleep(2)
print("end of an application")    
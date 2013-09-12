#coding=utf-8
#测试__call__方法
class CallTst():
    def __init__(self):
        print "i am init fun" 

    def __call__(self, x, y):
        print "i am call fun "+x+y

x = CallTst()
x("2","3")
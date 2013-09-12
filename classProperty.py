#coding=utf-8
#类属性：
class CP():
    dataMap = {"a":11, "b":22, "c":33}
    def x(self):
        print self.dataMap

print CP.dataMap
ccp = CP()
print ccp.dataMap
ccp.x()

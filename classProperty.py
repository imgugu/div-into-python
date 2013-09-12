#coding=utf-8
#类属性：
class CP():
    dataMap = {"a":11, "b":22, "c":33}
    def x(self):
        return self.dataMap

print CP.dataMap
ccp = CP()
print ccp.dataMap
print ccp.x()

ccp.dataMap = None
print ccp.dataMap
print CP.dataMap

CP.dataMap = None
print CP.dataMap
#coding=utf-8
#测试__del__方法
class Study:
    def __init__(self,name=None):
        self.name =name
    def __del__(self):
        print"I am away,baby!"
    def say(self):
        print self.name
    def doit(self):
        print "do it"

study = Study("zhuzhengjun")
study.say()
study.doit()
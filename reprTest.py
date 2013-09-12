#测试__repr__方法
class Study:
    def __init__(self,name=None):
        self.name =name
    def __del__(self):
        print self.name+",I am away,baby!"
    def say(self):
        print self.name
    def __repr__(self):
        return"Study('jacky')"

study = Study("zhuzhengjun")
study.say()
print study #如果定义了__repr__方法，而未定义__str__方法，则__str__=__repr__
x = eval(repr(study))
x.say()
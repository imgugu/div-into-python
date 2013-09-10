#__author__ = 'jlgu'

class Student():
    def __init__(self):
        self.myName = "jlgu"
    def showName(self):
        return self.myName

stu = Student()
print stu.showName()
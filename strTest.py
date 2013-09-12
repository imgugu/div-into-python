#coding=utf-8
#测试__str__方法

class PhoneNumber:
    def __init__(self,number):
         self.areaCode=number[1:4]
         self.exchange=number[6:9]
         self.line=number[10:14]

    def __str__(self):
        return "(%s) %s-%s"%(self.areaCode,self.exchange,self.line)

def test():
     newNumber = raw_input("Enter phone number in the form. (123) 456-7890: \n")
     phone = PhoneNumber(newNumber)
     print "The phone number is:"
     print phone

if __name__=="__main__":
     test()
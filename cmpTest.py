#测试__cmp__方法
class Study:
     def __cmp__(self, other):
         if other > 0 :
             return 1
         elif other < 0:
             return - 1
         else:
             return 0

study = Study()
if study > -10 : print 'ok1'
if study < -10 : print 'ok2'
if study == 0 : print 'ok3'
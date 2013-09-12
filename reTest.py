#coding=utf-8
#正则表达式：
import re

#匹配整个单词
print "匹配整个单词:"
s = '100 BROAD ROAD'
print re.sub('ROAD$', 'RD.', s)
s = '100 BROAD'
print re.sub('ROAD$', 'RD.', s)
print re.sub('\\bROAD$', 'RD.', s)

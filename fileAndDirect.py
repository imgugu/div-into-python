#coding=utf-8
#文件和目录：

import os
#分割路径名
print "#分割路径名："
print os.path.expanduser("~")
print os.path.split("c:\\music\\ap\\mahadeva.mp3")
(filepath, filename) = os.path.split("c:\\music\\ap\\mahadeva.mp3")
print filepath
print filename
(shortname, extension) = os.path.splitext(filename)
print shortname
print extension[1:]

#列出目录
print "#列出目录："
dirname = "D:\\pycode\\pycharm\\div-into-python"
print os.listdir(dirname)
print [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, f))]
print [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]


#在目录中找出适配的文件
print "#在目录中找出适配的文件"
def listDirectory(directory, fileExtList):
    "get list of file info objects for files of particular extensions"
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f) for f in fileList if os.path.splitext(f)[1] in fileExtList]
    return fileList

print listDirectory(dirname,[".py",".txt"])

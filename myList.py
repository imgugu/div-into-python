#伪造一个列表类List：
class MyList():
    def __init__(self,mlist=None):
        self.data = mlist

    def __getitem__(self, item):
        if item < len(self.data):
            return self.data[item]

    def __setitem__(self, key, value):
        if key < len(self.data):
            self.data[key] = value

    def __delitem__(self, key):
        if key in self.data:
            self.data.remove(key)

    def __str__(self):
        return str(self.data)

x = MyList(["a","b","c","d"])
print x[1]
print x
del x["a"]
print x
x[1] = "-"
print x
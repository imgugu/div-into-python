#冒泡算法

array = [1,99,23,59,29,44,77,60]
for j in range(len(array)-1,-1,-1):
    for i in range(j):
        if array[i]>array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]
print array
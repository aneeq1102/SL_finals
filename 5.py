import operator
import functools

d = dict()
text = open('sample.txt','r')

for line in text:
    line = line.strip()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
arr1 = []
wlengths = []
for key in list(d.keys()):
    arr1.append((d[key],key))
    wlengths.append(d[key])
arr1.sort(reverse = True)

for i in range(min(10,len(arr1))):
    print(arr1[i][1],':',arr1[i][0])

print('odd numbers:',[x for x in wlengths if x%2 == 1])
print('Average length',(functools.reduce(operator.add,wlengths))/len(wlengths))

class Rev:
    def __init__(self,in_str):
        self.str = in_str

    def reversed(self):
        self.arr = self.str.split(" ")
        self.arr.reverse()
        for i in self.arr:
            print(i + " ",end="")
def isVowel(ch):
    ch = ch.upper()

    if(ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return True
    return False

def countVowels(str):
    count = 0
    for i in str:
        if(isVowel(i)):
            count += 1

    return count
def sortStrings(n,arr):
    vowCounts = []
    for str in arr:
        vowCounts.append((countVowels(str),str))

    vowCounts.sort(reverse = True)
    res = []
    for i in range(0,n):
        res.append(vowCounts[i][1])
    return res

n = int(input('enter the number of strings to insert'))
strings = []
for i in range(0,n):
    str = input('enter string')
    strings.append(str)

stringsmod= sortStrings(n,strings)
stringobjs = []

for i in stringsmod:
    stringobjs.append(Rev(i))

for i in stringobjs:
    i.reversed()
    print('\n')

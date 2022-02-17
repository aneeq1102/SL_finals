conversions = []
def c2k(c):
    return c+273.15
def c2f(c):
    return c*9/5+32
def f2k(f):
    return (f-32)*5/9+273.15
def f2c(f):
    return (f-32)*5/9
def k2c(k):
    return k - 273.15
def k2f(k):
    return (k + 32*5/9 - 273.15)*9/5

def doConversions():
    while True:
        t = input('enter 1 to continue,0 to exit')
        if t == '0':
            break
        unitFrom = input('enter unit to convert from c,k or f')
        unitTo = input('enter unit to convert to c,k or f')
        mag = float(input('enter magnitude'))
        conv = 0
        if unitFrom == 'c' and unitTo == 'k':
            conv = c2k(mag)
            conversions.append("c -> k,{} -> {}".format(mag,conv))
        elif unitFrom == 'c' and unitTo == 'f':
            conv = c2f(mag)
            conversions.append("c -> f,{} -> {}".format(mag,conv))
        elif unitFrom == 'f' and unitTo == 'c':
            conv = f2c(mag)
            conversions.append("f -> c,{} -> {}".format(mag,conv))
        elif unitFrom == 'f' and unitTo == 'k':
            conv = f2k(mag)
            conversions.append("f -> k,{} -> {}".format(mag,conv))
        elif unitFrom == 'k' and unitTo == 'f':
            conv = k2f(mag)
            conversions.append("k -> f,{} -> {}".format(mag,conv))
        elif unitFrom == 'k' and unitTo == 'c':
            conv = k2c(mag)
            conversions.append("k -> c,{} -> {}".format(mag,conv))
        elif unitFrom == unitTo:
            conv = mag
            if unitFrom == 'c':
                conversions.append("c -> c,{} -> {}".format(mag,conv))
            elif unitFrom == 'f':
                conversions.append("f -> f,{} -> {}".format(mag,conv))
            elif unitFrom == 'k':
                conversions.append("k -> k,{} -> {}".format(mag,conv))
        else:
            print('invalid input')

def fromConv(conversions):
    unit = input('enter unit to obtain from conversions')
    res = []
    if unit == 'c':
        for conversion in conversions:
            if conversion[0] == 'c':
                res.append(conversion)
    elif unit == 'f':
        for conversion in conversions:
            if conversion[0] == 'f':
                res.append(conversion)
    elif unit == 'k':
        for conversion in conversions:
            if conversion[0] == 'k':
                res.append(conversion)
    return res

def toConv(conversions):
    unit = input('enter unit to obtain from conversions')

    if unit == 'c':
        for conversion in conversions:
            if conversion[5] == 'c':
                res.append(conversion)
    elif unit == 'f':
        for conversion in conversions:
            if conversion[5] == 'f':
                res.append(conversion)
    elif unit == 'k':
        for conversion in conversions:
            if conversion[5] == 'k':
                res.append(conversion)

    return res
def sort(conversions):
    a1 = input('enter 1 to sort by from conversions,2 to sort by to conversions')

    if a1 == '1':
        return fromConv(conversions)

    elif a1 == '2':
        return toConv(conversions)
    else:
        print('invalid input')

doConversions()
print(sort(conversions))

def findMaxRec(A,n):
    if n==1:
        return A[0]
    return max(A[n-1],findMaxRec(A,n-1))

y = []

while True:
    temp = input('enter number to append,e to exit')

    if temp == 'e':
        break;

    y.append(int(temp))

print('max is',findMaxRec(y,len(y)))

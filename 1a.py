x = []



while True:
    t = input('enter a number,e to exit:\n')

    if(t == 'e'):
        break;
    x.append(int(t))

print('input list:')
print(x)
uniq = []
for i in x:
    if i not in uniq:
        uniq.append(i)
print('unique elements:')
print(uniq)
evens = [x*2 for x in range(0,10)]
print('even nums')
print(evens)

rev_evens = []

for i in reversed(evens):
    rev_evens.append(i)
print(rev_evens)

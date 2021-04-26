n, m = map(int, input('').split(' '))
maxnum = []
for i in range(n):
    a = max([int(i) for i in input('').split(' ')])
    maxnum.append(a)
s = sum(maxnum)
print(s)
div = 0
for i in maxnum:
    if s % i == 0:
        div = 1
        print(i,end = ' ')
if  div == 0:
    print('-1')
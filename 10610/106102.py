k = int(input(''))
string = input('')
pervious = ''
numlist = []
num = 0
Max = 0
ans = 0

if string[0].isupper():
    pervious = 'up'
else:
    pervious = 'low'
num += 1

for i in range(1,len(string)):
    if string[i].isupper() and pervious =='up':
        num += 1
    elif string[i].islower() and pervious =='low':
        num += 1
    else:
        numlist.append(num)
        if string[i].isupper():
            pervious = 'up'

        else:
            pervious = 'low'
        num = 1
numlist.append(num)
print(numlist)

anslist = []
for i in range(0,len(numlist)):
    for j in range(i+1,len(numlist)+1):
        temp = [numlist[k] for k in range(i,j)]
        anslist.append(temp)

for i in anslist:
    if i[0] >= k and i[-1] >= k:
        if len(i) - 2 == len([i[j] for j in range(1,len(i)-1) if i[j] == k]):
            print(i)
            Max = k*len(i)
            ans = max(ans,Max)

print(ans)
n, m = map(int ,input('').split(' '))
ans = []
for i in range(n):
    temp = list(map(int, input('').split(' ')))
    ans.append(temp)
a = sum([max(i) for i in ans])
print(a)
answer = [max(i) for i in ans]
answer = [i for i in answer if i % a == 0]
if len(answer) == 0:
    print('-1')
else:
    for i in answer:
        print(i, end = ' ')
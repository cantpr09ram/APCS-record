import array

ans = array.array('b',[0 for i in range(10000000)])

times = int(input(''))
for i in range(times):
    start, end = map(int, input('').split(' '))
    for i in range(start, end):
        if ans[i] == 1:
            pass
        else:
            ans[i] = 1
print(ans.count(1))
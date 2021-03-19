ans = []
n = int(input(''))
for i in range(n):
    temp = [int(i) input().split(' ')]
    if ans == []:
        ans.append(temp)
    else:
        for i in ans:    
            if temp[0] < i[0] and temp[1] < i[1]:#左小右小
                i[0] = temp[0]
            elif temp[0] < i[1] and temp[1] > i[1]:
                i[1] = temp[1]
            elif
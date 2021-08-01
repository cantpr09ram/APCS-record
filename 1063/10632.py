n = int(input(''))
group = [int(i) for i in input('').split(' ')]
friend = 0

for i in range(n):
    if group[i] != -1:
        j = i
        while True:
            a = j
            j = group[j]
            group[a] = -1
            if j == i:
                break
        friend += 1
print(friend)
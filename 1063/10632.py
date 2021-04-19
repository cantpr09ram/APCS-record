n = int(input(''))
group = [int(i) for i in input('').split(' ')]
friend = 0

for i in range(len(group)):
    a = group[i]
    fri = []
    test = True
    while test:
        f = group[a]
        if i == f:
            friend += 1
            group.pop(a)
            for j in fri:
                group.pop(j)
            fri.clear()
            test = False
        else:
            fri.append(f)
            a = f
    
print(friend)
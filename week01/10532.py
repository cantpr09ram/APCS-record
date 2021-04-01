def abc(a : list) -> list:#翻轉
    return reversed(a)

def efg(a : list, x : int ,y : int) -> list:#旋轉
    b = [[0 for i in range(y)] for j in range(x)]
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[j][i] = a [i][j]
    return reversed(b)
while True:
    try:
        d = [int(i) for i in input('').split(' ')]
        r = d[0]
        c = d[1]
        m = d[2]

        list1 = []
        for i in range(r):
            temp = list(input('').split(' '))
            list1.append(temp)

        act = [int(i) for i in input('').split(' ')]

        for i in reversed(act):
            if i == 1:
                list1 = abc(list1)
            else:
                list1 = efg(list1,len(list1),len(list1[0]))

        print(f'{len(list1)} {len(list1[0])}')
        for i in range(len(list1)):
            for j in range(len(list1[0])):
                print(list1[i][j],end = ' ')
            print()
    except Exception:
        pass
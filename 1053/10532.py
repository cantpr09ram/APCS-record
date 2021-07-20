while True:
    try:
        r, c, m = map(int,input('').split(' '))
        list1 = []
        for i in range(r):
            list1.append(list(map(int,input('').split(' '))))
        
        print(list1)
    
        act = [int(i) for i in input('').split(' ')]

        for i in reversed(act):
            if i == 1:
                list1.reverse()
            else:
                b = []
                for i in range(c-1, -1, -1):
                    b.append([])
                    for j in range(r):
                        b[-1].append(list1[j][i])
                c, r = r, c
                list1 = b

        print(f'{r} {c}')
        for i in range(r):
            for j in range(c):
                print(list1[i][j],end = ' ')
            print()
    except :
        pass
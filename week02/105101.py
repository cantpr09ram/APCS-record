try:    
    list1 = list(map(int ,input('').split(' ')))
    list1.sort()
    a = list1[0]
    b = list1[1]
    c = list1[2]

    if a + b <= c:
        print(f'{a} {b} {c}')
        print('No')
    elif a**2 + b**2 < c**2:
        print(f'{a} {b} {c}')
        print('Obtuse')
    elif a**2 + b**2 == c**2:
        print(f'{a} {b} {c}')
        print('Right')
    else:
        print(f'{a} {b} {c}')
        print('Acute')
except Exception:
    pass
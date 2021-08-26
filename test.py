'''
a = [[1 for j in range(5)], 
     [2 for j in range(5)],
     [3 for j in range(5)],
     [4 for j in range(5)],
     [5 for j in range(5)],
     [6 for j in range(5)]]
for i in range(6):
    for j in range(5):
        print(a[i][j], end='')
    print()

print()

x, y = 0, 0
while True:
    if x == 6:
        print() 
        x = 0
        y += 1

    print(a[x][y] ,end='')

    x += 1
    if x==6 and y==4:
        break
    '''
'''
a = 1
a = b
print(b)
for i in range(5):
    if a == 1:
        print('1')
        pass
    elif a == 1:
        print('2')
    else:
        print('x')
        '''
a, b,c,d = 0, 0 ,0 ,1

for i in range(4):
    c, d, a, b = b, c, d, a
    print(a,b,c,d)
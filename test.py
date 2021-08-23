a = [[1 for j in range(5)] for i in range(6)]
for i in range(6):
    for j in range(5):
        print(a[i][j], end='')
    print()

print()

x, y = 0, 0
while True:
    if y == 4:
        print() 
        y = 0
        x += 1

    print(a[y][x] ,end='')

    y += 1

    if x == 4 and y == 5:
        break
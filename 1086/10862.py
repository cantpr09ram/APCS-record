"""
1. find the minNum (finished)
2. start serach and add number to string (working)
3. stop
"""
_map = []
r, c = map(int, input('').split(' '))
for i in range(r):
    
    temp = []
    temp = [int(i) for i in input('').split(' ')]
    _map.append(temp)

minNum = 1000001
numx, numy = 0, 0
for i in range(r):
    for j in range(c):
        if _map[i][j] < minNum:
            minNum = _map[i][j]
            numx, numy = i, j
"""up, down,  right, left"""
#print(minNum)

now = -1
ans = 0

while True:
    moving = False

    if numx - 1 >= 0 : #up
        if _map[numx -1][numy] > now:
            now = _map[numx][numy]
            numx -= 1
            moving = True
            ans += now
            #print(now)

    if numx + 1 < r : #down
        if _map[numx + 1][numy] > now:
            now = _map[numx][numy]
            numx += 1
            moving = True
            ans += now
            #print(now)

    if numy - 1 >= 0 : #left
        if _map[numx][numy - 1] > now:
            now = _map[numx][numy - 1]
            numy -= 1
            moving = True
            ans += now
            #print(now)

    if numy + 1 < c : #right
        if _map[numx][numy+1] > now:
            now = _map[numx][numy+1]
            numy += 1 
            moving = True
            ans += now
            #print(now)

    if moving == False:
        print(ans + minNum)
        break
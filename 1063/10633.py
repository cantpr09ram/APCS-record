print()
a = int(input(''))
dirction = int(input(''))
dit_list = [[1,0],[-1,0],[0,-1],[0,1]]  #(up, down, left, right) = (1,3,0,2)
"""
thinking

lurd
urdl
rdlu
dlur
  => dlur = lurd = urdl = rdlu
  => 3210 = 0123 = 1230 = 2301 
"""
arr = []
temp = []
for i in range(a):
    temp = [int(i) for i in input('').split(' ')]
    arr.append(temp)

numdirx, numdiry = a // 2, a // 2
step = 0
limit = 0 #limit of step  
_round = 0 #if step == limit. round += 1

for i in range(a**2):
    print(f'      dir {dirction} {numdirx} {numdiry}')
    print(arr[numdirx][numdiry])
    step += 1
    limit += 1

    if limit == 2:#轉彎
        _round += 1
        step = 0
    else:
        pass
    if #e改方向
    numdirx += dit_list[dirction][0]
    numdiry += dit_list[dirction][1]

    if dirction > 3:#不要過頭
        dirction = 0
    else:
        pass
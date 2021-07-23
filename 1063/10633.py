print()
a = int(input(''))
dirction = int(input(''))
dit_list = [[0,-1],[-1,0],[0,1],[1,0]]  #(left,up, down,  right) = (,0,1,2,3)
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
step = 0 #
limit = 1 #同方向要走幾步
_round = 0 #通步數要轉幾次

'''
兩個方向後同方向步數加一
1.轉彎的時間
2.加步數的時間
'''
print()
print(arr[numdirx][numdiry])

for i in range(a**2-1):

    step += 1
    if _round == 2:#加步數
        _round = 0
        step = 0
        limit += 1 
        dirction += 1   

    numdirx += dit_list[dirction][0]
    numdiry += dit_list[dirction][1]

    if step == limit: #改方向
        dirction += 1
        _round += 1

    if dirction > 3:#不要過頭
        dirction = 0
    print(dirction,numdirx,numdiry)
    print(arr[numdirx][numdiry])
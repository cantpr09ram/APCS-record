a = int(input(''))
dirction = int(input(''))
dit_list = [[0,-1],[-1,0],[0,1],[1,0]]  #(left,up, down,  right) = (0,1,2,3) => (left, up, right, down) = (,0,1,3,2)
"""
thinking

lurd
urdl
rdlu
dlur
  => dlur = lurd = urdl = rdlu
  => 2013 = 0132  = 
"""
arr = []
temp = []
for i in range(a):
    temp = [int(i) for i in input('').split(' ')]
    arr.append(temp)

numdirx, numdiry = a // 2, a // 2
step = 0 #
limit = 1 #同方向要走幾步
ans = ''
'''
兩個方向後同方向步數加一
1.轉彎的時間
2.加步數的時間
'''
while True:
    for j in range(2):
        for k in range(limit):
            if len(arr) == 0:
                break
            else:
                x = arr[numdirx][numdiry]
                arr.remove(0)
                print(x)
                numdirx += dit_list[dirction][0]
                numdiry += dit_list[dirction][1]
        dirction = (dirction + 1) % 4
    limit += 1
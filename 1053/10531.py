a = int(input(''))
# 10
list1 = list(map(int, input('').split(' ')))
# 0 11 22 33 55 66 77 99 88 44
list1.sort()
mx = 101
mi = -1
for i in list1:
    print(i,end = ' ')
    if i >= 60 and i < mx:
        mx = i
    elif i < 60 and i > mi:
        mi = i
print()    

if mi == -1:
    print('best case')
else:
    print(mi)

if mx == 101:
    print('worst case')
else:
    print(mx)  
#ZEROJUDGE
"""
您的答案為: best ca ...略
正確答案為: 80

您的答案為: best cas ...略
正確答案為: 100

請勿輸出題目未要求的文字: 
worst case
"""
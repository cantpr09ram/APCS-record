a = int(input(''))
# 10
list1 = list(map(int, input('').split(' ')))
# 0 11 22 33 55 66 77 99 88 44
list1.sort()

for i in list1:
    print(i,end = ' ')
print()    

for i in reversed(list1):
    if i < 60:
        print(i)
        break
    elif i == list1[0]:
        print('best case')

for i in list1:
    if i >= 60:
        print(i)
        break
    elif i == list1[-1]:
        print('worst case')
#ZEROJUDGE
"""
您的答案為: best ca ...略
正確答案為: 80

您的答案為: best cas ...略
正確答案為: 100

請勿輸出題目未要求的文字: 
worst case
"""
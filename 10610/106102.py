k = int(input(''))
string = input('')

upper = 0
lower = 0
ans = 0
Max = 0

for i in string:
    if i.isupper():
        upper += 1
    else:
        lower += 1
    
    if upper < k and lower < k:
        pass
    elif upper == k and lower == k:
        Max += 1
    else:
        ans = max(ans,Max)
        Max = 0
print(ans*k)
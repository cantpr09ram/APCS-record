a, b = map(int, input('').split(' '))
n = int(input(''))
ans = 0
for i in range(n):
    shop = [int(i) for i in input('').split(' ') if abs(int(i)) == a or b]
    if shop.count(a) > shop.count(-a) and shop.count(b) > shop.count(-b):
        ans += 1
print(ans)
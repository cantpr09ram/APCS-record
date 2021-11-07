def test (d : int) -> bool:
    scope, num = 0, 0
    global n, k ,p
    i = 0
    while i <= n:
        scope = p[i] + d
        num += 1
        if num > k:
            return False
        if p[n - 1] <= scope and num <= n:
            return True
        while scope <= p[i]:
            i += 1
    return False

n, k = map(int, input("").split(" "))
p = [int(i) for i in input("").split()]
p.sort()

right = 0
left = (p[n-1] - p[0]) // k + 1
while left >= right:
    mid = (left + right) // 2
    if test(mid):
        right = mid
    else:
        left = mid + 1
    if right == left:
        break
print(right)
n, m, k = map(int, input('').split(' '))
ans = [i for i in range(1, n+1)]

die = 0
while (k != 0):
    die = (die + m) % n
    n =- 1
    print(die)
    ans.remove(die)
    die %= die
    k-1
    if k == 0:
        print(die)
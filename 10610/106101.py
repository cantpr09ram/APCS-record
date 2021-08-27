def AND(a : int, b : int) -> int:
    if a & b > 0:
        return 1
    else:
        return 0

def OR(a : int, b : int) -> int:
    if a | b > 0:
        return 1
    else:
        return 0

def XOR(a : int, b : int) -> int:
    if a > 0:
        a = 1
    if b > 0:
        b = 1
    if a != b:
        return 1
    else:
        return 0
a, b, c = map(int, input('').split(' '))
print(a,b,c)
bools = False
if AND(a,b) == c:
    print('AND')
    bools = True
if OR(a,b) == c:
    print('OR')
    bools = True
if XOR(a,b) == c:
    print('XOR')
    bools = True

if bools == False:
    print('IMPOSSIBLE')
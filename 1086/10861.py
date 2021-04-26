h = 0
g = 0
for i in range(2):
    h_score = sum([int(i) for i in input('').split(' ')])
    g_score = sum([int(i) for i in input('').split(' ')])
    if h_score > g_score:
        h += 1
    else:
        g += 1
    print(f'{h_score}:{g_score}')


if h == 2:
    print('Win')
elif g == 2:
    print('Lose')
else:
    print('Tie')
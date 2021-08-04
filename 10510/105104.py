game = []
for i in range(9):
    game.append([j for j in input('').split(' ')])

a = int(input(''))

i = 0
j = 0
good = 0
bad = 0
score = 0
soft_bag = [0 for i in range(4)]


while a != 0:
    i += 1
    if i > 8:
        i = i%8
        j += 1

    player = game[i][j]
    if len(player) == 1:
        pass
    elif player == 'FO' or player == 'SO' or player == 'GO':
        good += 1
        a -= 1
        if good == 3:
            good = 0
            soft_bag = []
    elif player == 'HR':
        score += 3
        soft_bag = []
    else:
        run = int(player[0])
        for i in range(run):
            soft_bag[i+1] = soft_bag[i]
            soft_bag[0] = 1
            if soft_bag[3] == 1:
                score += 1
                soft_bag[3] = 0

print(score)      
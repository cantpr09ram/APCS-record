#solution1 5%
game = []
for i in range(9):
    game.append([j for j in input('').split(' ')])

a = int(input(''))
i = 0
j = 1
good = 0
score = 0
one, two , three, four = 0, 0, 0, 0
run = 0


while a != 0:
    if i == 9:
        i = 0
        j += 1

    player = game[i][j]
    i += 1
    if len(player) == 1:
        pass

    elif player == 'FO' or player == 'SO' or player == 'GO':
        good += 1
        a -= 1
        if good == 3:
            one = 0
            two = 0 
            three = 0 
            four = 0
            good = 0

    elif player == 'HR':
        run = 4

    else:
        run = int(player[0])
        four = 1
        for k in range(run):
            three, four, one, two = two ,three, four, one
            if four == 1:
                score += 1
                four = 0
print(score)      
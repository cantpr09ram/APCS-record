n, m, k = map(int, input('').split(' '))
people = [i+1 for i in range(n)]
die = 0
for i in range(k):
    die = (die + m - 1)%len(people)
    people.pop(die)

print(people[(die)%len(people)])

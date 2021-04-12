ans = [int(i) for i in input('')]

odd = sum([ans[i] for i in range(len(ans)) if i%2 == 1])
even = sum([ans[i] for i in range(len(ans)) if i%2 == 0])
print(abs(even - odd))
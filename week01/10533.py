"""
i
@@@@@@@@
i-1
  #########                1
  %%%                      2
&&&&&&&&                   3
                $$$$       4
"""
answer = 0
while True: 
    try:
        ans = []
        n = int(input(''))
        for i in range(n):
            f,n = list(map(int, input().split(' ')))
            ans.append([f,n])
        ans.sort()
        for i in range(1, len(ans)):
            if (ans[i][0] <= ans[i-1][0]) and (ans[i][1] < ans[i-1][1]): #1
                ans[i][1] = ans[i-1][1]
                ans.remove(ans[i-1])
            elif ans[i][1] <= ans[i-1][0]: #4 ok
                pass
#count
        for i in ans:
            answer += (i[1] - i[0])
        print(answer)
    except Exception:
        break
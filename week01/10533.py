"""
i
     @@@@@@@@
i-1
#########                  1

!!!!!!!!!!!!!!!!           2

     &&&&&&&&              3 ok 

   &&&&&&&&&&&&            4
$$                         5
"""
while True: 
    try:
        ans = []
        answer = 0
        n = int(input(''))
        for i in range(n):
            f,n = list(map(int, input().split(' ')))
            ans.append([f,n])
        ans.sort()
        #print(ans)
        for i in range(1, len(ans)):
            if ans[i][0] > ans[i-1][0]:
                if ans[i][1] < ans[i-1][1]: #2
                    #print('2')
                    #print(ans)
                    ans[i][0] = ans[i-1][0]
                    ans[i][1] = ans[i-1][1]
                    ans[i-1] = []
                elif ans[i-1][1] < ans[i][0]:
                    pass
                else:
                    #print('1')
                    #print(ans)
                    ans[i][0] = ans[i-1][0]
                    ans[i-1] = []

            else: #4
                if ans[i-1][1] > ans[i][1]:
                    ans[i-1][1] = ans[i][1]
                    ans[i-1] = []
                    #print('4')
                    #print(ans)
                else:
                    print('3')
                    print(ans)
                    pass

#count
        #print(ans)
        for i in ans:
            if i != []:
                answer += (i[1] - i[0])
        print(answer)
    except Exception:
        break
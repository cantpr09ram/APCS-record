ans = []
"""
  @@@@@
   ######                    1
%%%%%%                       2
  &&                         3
!!!!!!!!!                    4
                $$$$         5
"""
while True:
    try:
        ans = []
        n = int(input(''))
        for i in range(n):
            temp = list(map(int, input().split(' ')))
            
            if len(ans) == 0:
                ans.append(temp)
            else:
                test = False
                for i in ans:
                    if temp[0] < i[0] and (temp[1] > i[0] and temp[1] <i[1]):
                        i[0] = temp[0]
                        test = True
                        
                    elif temp[1] > i[1] and (temp[0] > i[0] and temp[0] < i[1]):
                        i[1] = temp[1]
                        test = True
                        
                    elif temp[0] > i[0] and temp[1] < i[1]:
                        test = True
                        
                    elif temp[0] < i[0] and i[1] < temp[1]:
                        i[0] = temp[0]
                        i[1] = temp[1]
                    elif test == False:
                        ans.append(temp)
                        test = True
                        

        """ count """
        answer = 0
        for i in ans:
            answer += (i[1] - i[0])
    except Exception:
        break
import  random
try:
    for i in range(int(input())):
        k =int(input())
        arr =[]
        count=0
        # I=[]
        # J=[]
        flag=0
        for i in range(8):
            arrt=[]
            for j in range(8):
               arrt.append(str('X'))
            arr.append(arrt)

        # x=0
        # y=0
        # # x=random.randrange(0,8)
        # # y=random.randrange(0,8)
        # arr[x][y]='O'
        # for test in range(64):
        #     if x-1>=0 :
        #         arr[x - 1][y] = 'X'
        #         if y - 1 >= 0:
        #             arr[x - 1][y - 1] = 'X'
        #         if y + 1 < 8:
        #             arr[x - 1][y + 1] = 'X'
        #     if  y-1>=0:
        #         arr[x][y - 1] = 'X'
        #         if x + 1 < 8:
        #             arr[x + 1][y - 1] = 'X'
        #     if  x+1<8:
        #         arr[x + 1][y]= 'X'
        #         if y + 1 < 8:
        #             arr[x + 1][y + 1] = 'X'
        #     if  y+1<8:
        #         arr[x][y + 1]= 'X'
        #     else:
        #         pass

        # for i in range(k):

        #      arr[i][i+1] = '.'

        for i in range(8):
            for j in range(8):
                arr[i][j]='.'
                count+=1
                if count>=k:
                    flag=1
                    break
            if flag==1:
                break

        arr[0][0] = 'O'
                # count+=1
                # # if i==0 and j==0 :
                # #     pass
                # # elif count<=k:
                # #     arr[i][j]='.'

                # if count>k and flag==0:
                #     j=k+1
                #     if j>=7:
                #        j=0
                #        i=i+2
                #     else:
                #        j=k+1
                #        i=i+1
                #     flag=1
                # j=4
                # if flag==1:
                #     arr[i][j]='.'

            # ii = random.randrange(-1, 1)
            # jj = random.randrange(-1, 1)
            # i=abs(xx+ii)
            # j=abs(yy+jj)
            # I.append(i)
            # J.append(j)
            # xx=i
            # jj=j
            # if i==x and j==y:
            #     flag=1
            # elif I and J : # i==I[test2-1] and j==J[test2] :
            #     flag=0
            #     for test3 in range(KK):
            #         if i==I[test3] and j==J[test3]:
            #             flag=1

            # if flag==0:
            #     arr[i][j] = '.'
            #     for test in range(64):
            #         if i - 1 >= 0:
            #             arr[i - 1][j] = 'X'
            #             if j - 1 >= 0:
            #                 arr[i - 1][j - 1] = 'X'
            #             if j + 1 < 8:
            #                 arr[i - 1][j + 1] = 'X'
            #         if j - 1 >= 0:
            #             arr[i][j - 1] = 'X'
            #             if i + 1 < 8:
            #                 arr[i + 1][j - 1] = 'X'
            #         if i + 1 < 8:
            #             arr[i + 1][j] = 'X'
            #             if j + 1 < 8:
            #                 arr[i + 1][j + 1] = 'X'
            #         if j + 1 < 8:
            #             arr[i][j + 1] = 'X'
            #         else:
            #             pass
            # else:
            #     pass

        for i in range(8):
           for j in range(8):
                print(arr[i][j],end='')
           print()
        # print('\n')


except Exception:
    pass

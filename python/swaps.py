# try :
for k in range(int(input())):
        n= int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        flag=False
        cost=0
        c=a+b
        a.sort()
        b.sort()
        if a==b:
            print(cost)
        else:
            c.sort()
            N=len(c)
            i=0
            while i<N:
                if i==N-1:
                    break
                elif c[i]==c[i+1]:
                    cost=0
                    i=i+2
                else:
                    cost=-1
                    break
            if(cost==0):
                for i in range(n):
                    for j in range(n):
                        if j[j]==j[j+1]:
                            cost=min(a[i],j[j])
                        else:












                # i = 0
                # while i < n:
                    # if i == n- 1:
                    #     break
                    # elif a[i] == a[i + 1]:
                    #     cost = cost+1
                    #     i = i + 1
                    # else:
                    #     i = i + 1

                print(cost)
            else:
                print(cost)


# except Exception:
#     pass

for _ in range(int(input())):
    n= int(input())
    a=list(map(int,input().split()))
    # h=list()
    # l=list()
    # flag=False
    ans=0
    for i in range(1,n):
        if a[i-1]>a[i]: 
            ans+=a[i-1]-a[i]


        #     h.append(a[i])
            
        #     if a[i-1]>xx:
        #         xx=a[i-1]
        #     flag=True
        # if a[i]>=xx and flag==True :
        #     mm=min(h)
        #     l.append(xx-mm)
        #     h=list()
        #     xx=a[i]
        #     flag=False
        # elif flag==True and i==n-1:
        #     mm=min(h)
        #     l.append(xx-mm)
            


    print(ans)
    # if l:
    #     print(sum(l))
    # else:
    #     print(0)



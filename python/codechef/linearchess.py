for _ in range(int(input())):
    N,K= map(int,input().split())
    P=list(map(int,input().split()))
    count=set()
    Temp=0
    flag=False
    i=0
    while i<N:
        if flag==False:
            if P[i]<=K//2:
                Y=P[i]
                s=P[i]
                flag=True
            else:
                i+=1
                continue
        Y=Y+s
        Temp+=1
        if Y==K:
            count.add(Temp)
            Temp=0
            i+=1
            flag=False
        elif Y>K:
            i+=1
            flag=False
            Temp=0
        
   
    if count:
        print(sum(count))
    else:
        print(-1)


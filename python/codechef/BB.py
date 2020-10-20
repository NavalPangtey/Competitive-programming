for _ in range(int(input())):
    n=int(input())
    # X=list()
    # Y=list()
    for i in range(n):
        x,y=map(int,input().split())
    #     X.append(x)
    #     Y.append(y)
    
    # for i in range(n):
    #     if X[i]<0:
    #         X[i]=abs(X[i])
    #     if Y[i]<0:
    #         Y[i]=abs(Y[i])

    if n<=5:
        print(n)
    elif n>5:
        h=n
        sum=0
        while h>=6:
            h=h//2
            sum+=h

        
        print(n+sum)
        
    
for _ in range(int(input())):
    n,k= map(int,input().split())
    # n=5
    # k=1
    # a=[5 ,-1, 4 ,2 ,0]
    a=list(map(int,input().split()))
    if k%2!=0 or k==1:
        k=1
    else:
        k=2
    d =max(a)
    M=0
    while k:
        
        for i in range(n):
            a[i]=d-a[i]
            if a[i]>=M:
                M=a[i]
        d=M      
        k-=1

    for i in range(n):
        print(a[i],end=" ")
    print()

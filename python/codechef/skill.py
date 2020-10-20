for _ in range(int(input())):
    a,d,k,n,inc=map(int,input().split())
    arr=list()
    for i in range(1,n+1):
        if i%k==0:
            d+=inc
        arr.append(a)
        a+=d
    print(arr[-1])



for _ in range(int(input())):
    n,k=map(int,input().split())

    if k>n:
        print(k-n)
    elif k<=n:
        a=(n-k)%2
        print(a)

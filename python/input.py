T= int(input())

for i in range(T):
    N,S= map(int, input().split())
    if N%2==0:
        ans=0
        ans =ans+ (N//S)
        if N%S==0:
            print(ans)
        else:
            print(ans+1)

    else:
        ans=1
        N=N-1
        ans = ans+ (N//S)
        if N%S==0:
            print(ans)
        else:
            print(ans+1)





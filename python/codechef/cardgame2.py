for _ in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    l=len(set(c))
    if n==1:
        print(2)
    elif l==1:
        print(2)
    else:
        ans=n*(l-1)
        print(ans+ans)

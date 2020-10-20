for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print('T')
    else:
        s=sum(a)
        m=max(a)
        check=abs(s-m)
        if check<m:
            print('T')
        else:
            if s%2==0:
                print("HL")
            else:
                print('T')

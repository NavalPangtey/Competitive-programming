
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=[0]*n
    for i in range(n):
        t[i]=a[i]
    t.sort()
    m=t[0]
    flag=False
    for i in range(n):
        if a[i]!=t[i]:
            if a[i]%m!=0:
                flag=True
                break
    
    
    if flag:
        print("NO")
    else:
        print("YES")



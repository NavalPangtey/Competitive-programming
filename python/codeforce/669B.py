import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=list()
    b=[0]*n
    mm=max(a)
    ans.append(mm)
    maxi=-math.inf
    for k in range(n):
        if a[k]==mm:
            b[k]=1
            break
    GG=mm
    cc=-1
    for i in range(n-1):
        maxi=-math.inf
        for j in range(n):
            if b[j]!=1:       
                temp=math.gcd(GG,a[j])
                if temp>maxi:
                    maxi=temp
                    bb=a[j]
                    cc=j
            if j==n-1:
                GG=maxi
                ans.append(bb)
                if cc!=-1:
                    b[cc]=1

    for i in range(len(ans)):
        print(ans[i],end=" ")
    print()
             
    
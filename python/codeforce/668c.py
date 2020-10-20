import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    S=input()
    s=list(S)
    
    flag=False
    for i in range(n-k+1):
        zero=0
        one=0
        q=0
        for j in range(i,i+k):
          
            if s[j]=='0':
                zero+=1
            elif s[j]=='1':
                one+=1
            elif s[j]=='?':
                q+=1
        if one>k//2 or  zero>k//2:
            flag=True
            break
    if flag==True:
        print("NO")
    else:
        print("YES")



from functools import reduce
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 a=dict()
 f=0
 d=0
 for i in range(n):
    for j in range(i+1,n+1):
        s=l[i:j]
        # d+=1
        r=reduce(lambda x,y:x|y,s)
        a[r]=a.get(r,0)+1
        if a[r]!=1:
            f=1
            break
 print(a)
 if f==0:
     print("YES")
 else:
     print("NO")
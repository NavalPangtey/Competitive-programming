import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    Set=set()
    ans=[0]*n
    for i in range(n):
         if (abs(a[i]-k) not in Set):
             Set.add(a[i])
             ans[i]=1
    for i in range(n):
        print(ans[i],end=" ")
    print()
          
   
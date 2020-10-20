import math
for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    for i in range(len(p)):
        if (i+1)%2==0:
            temp=p[i]
            p[i]=p[i-1]
            p[i-1]=temp
    
    print(p)

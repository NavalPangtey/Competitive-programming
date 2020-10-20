import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif b>a:
        c=b-a
        d=c/10
        print(math.ceil(d))
    else:
        c=a-b
        d=c/10
        print(math.ceil(d))
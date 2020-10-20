import math
for _ in range(int(input())):
    a,b,x,y,n=map(int,input().split())
    while b>y and n>0:
        b-=1
        n-=1
    while a>x and n>0:
        a-=1
        n-=1
    print(f'{a} {b}')
    print(a*b)
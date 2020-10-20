import math
for _ in range(int(input())):
    x,y,k=map(int,input().split())
    sticks=k+k*y
    sticks=sticks+x-3
    ans=sticks//(x-1)
    print(ans+k)
    
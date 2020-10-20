import math
for _ in range(int(input())):
    n=int(input())
    count=0
    i=1
    while n>0:
        x=(2**i)-1
        m=(x*(x+1))//2
        n=n-m
        if n<0:
            break
        count+=1
        i+=1
    print(count)
    
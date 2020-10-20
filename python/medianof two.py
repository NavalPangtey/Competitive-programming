a=[]
b=[]

a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=a+b
c.sort()
print(c)
n=len(c)
if n%2==0:
    k=n//2
    median= (c[k-1]+c[k])/2
else:
    k = n //2
    median=c[k]

print(median)
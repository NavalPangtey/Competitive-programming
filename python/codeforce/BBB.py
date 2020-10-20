import math
n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=math.inf
k=1
while pow(k,n-1)<=pow(10,10):
    k+=1
k-=1
print(k)
for num in range(1,k+1):
    temp=0
    for j in range(n):
        temp+=abs(a[j]-pow(num,j))
    ans=min(ans,temp)

print(ans)





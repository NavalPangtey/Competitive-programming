n=int(input())
a=list(map(int,input().split()))

a.sort()
i=0
while i<n-1:
    temp=a[i]
    a[i]=a[i+1]
    a[i+1]=temp
    i+=2
ans=0
for j in range(1,n-1):
    if a[j]<a[j-1] and a[j]<a[j+1]:
        ans+=1
print(ans)
for n in a:
    print(n,end=" ")
print()


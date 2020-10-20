n= int(input())
arr=list(map(int,input().split()))

for _ in range(int(input())):
    r1,r2=map(int,input().split())
    add=100
    if r2<n-1:
        arr[r1]+=add
        arr[r2+1]=-add
    else:
        arr[r1]+=add
        arr.append(-add)

print(arr)
temp=0
for i in range(len(arr)):
    temp+=arr[i]
    arr[i]=temp
arr.pop()
print(arr)
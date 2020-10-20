def LIS(a,n):
    lis=[1]*n

    for i in range(1,n):
        for j in range(0,i):
            if a[i]>a[j] and lis[i]< lis[j] + 1 : 
                lis[i]=lis[j]+1

    return(max(lis))
a=list(map(int,input().split()))
n=len(a)

ans=LIS(a,n)
print(ans)
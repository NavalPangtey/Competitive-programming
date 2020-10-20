for _ in range(int(input())):
    n,k,l=map(int,input().split())
    arr=list()
    for y in range(l):
        for j in range(1,k+1):
            arr.append(j)
        if len(arr)>n:
            break
    
    if n>1 and k==1 and l>1:
        print(-1)
    elif len(arr)>=n :
        for i in range(n):
            print(arr[i],end=" ")
        print()
    else:
        print(-1)    


import math
for _ in range(int(input())):
    n,m=map(int,input().split())
    
    a=list(map(int,input().split()))
    mt=[[-math.inf for x in range(m)] for x in range(n)]
    
    mat=[]
    for i in range(n):
        c=list(map(int,input().split()))
        for j in range(len(c)):
            c[j]=a[i]+c[j]
            a[i]=c[j]
        mat.append(c)

    for j in range(m):
        arr=list()
        for i in range(n):
            arr.append(mat[i][j])
        arr.sort()
        arr.reverse()
        gg=set()
        for s in range(len((arr))):
            if arr[s] not in gg:
                gg.add(arr[s])
            else:
                arr[s]=-math.inf
        for k in range(len(arr)):
            for i in range(n):
                if mat[i][j]==arr[k] :
                    mt[i][j]=k+1    
            
    print(mt)
    for i in range(n):
        arr2=[]
        arr3=list()
        for j in range(m):
           arr2.append(mt[i][j])
           arr3.append(mat[i][j])
        mini=min(arr2)
        maxo=max(arr3)
        for j in range(m):
            if mt[i][j]==mini :
                if mat[i][j]==maxo:
                    mat[i][j]=-math.inf
                else:
                    break

    print(mat)
    count=0
    for i in range(n):
        for j in range(m):
            if mat[i][j]==-math.inf:
                count+=1
                break

    print(n-count)


    
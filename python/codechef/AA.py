for _ in range(int(input())):
    # n=input()
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    # matrix=[]
    # for i in range(n):
    #     YYY=str(input())
    #     yy=list(YYY)
    #     a=[]
    #     for j in range(m):
    #         a.append(yy[j])
    #     matrix.append(a)
    
    # for i in range(n):
    #     for j in range(m):
    #         print(matrix[i][j],end=" ")
    #     print()
    flag=False
    for i in range(n):
        if a[i]>k:
            print(-1)
            flag=True
            break
    if flag==False:
        sum=0
        count=0
        i=0
        while i<n:
          if sum+a[i]<k:
              sum+=a[i]
              if sum<=k and i==n-1:
                  count+=1
              i+=1
          elif sum+a[i]>k:
              sum=0
              count+=1
          elif sum+a[i]==k:
              sum=0
              count+=1
              i+=1


        print(count)

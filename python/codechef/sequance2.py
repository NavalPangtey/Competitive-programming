for _ in range(int(input())):
    N= int(input())
    arr=list(map(int,input().split()))
    help=set(arr)
    b=list()
    total=(2**N)-1
    M = 1000000007
    
    dic2= {}
    
    for k in b:
        dic2[k]=dic2.get(k,0)+1
    # total=0
    # for i in range(1,N+1):
    #     if i in help:
    #         for num in arr:
    #             if num==i:
    #                 total+=1
    #         dic2[i]=total%M
    #         total=0
    # print(dic2)
    
    # ans=list()
    # for i in range(1,N+1):
    #     if i in dic2:
    #         # crr=dic2.get(i)
    #         ans.append(dic2.get(i))
    #     else:
    #         ans.append(0)

    k=1
    for i in range(N):
        b.append(k)
        k=k*2
        k=k%M
    
    for i in reversed(range(N)):
        print(b[i],end=" ")
    print()
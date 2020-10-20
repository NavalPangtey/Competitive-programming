import  math
for _ in range(int(input())):
    n=int(input())
    mat=[]
    for i in range(n):
        a=list()
        a=list(map(int,input().split()))
        mat.append(a)
    # count=0
    # # for L in range(2,n+1):
    # flag=False

    # for i in range(n):
    #     for j in range(n):
    #         if mat[i][j]!=i*n+(j+1):
    #             flag=True
    #             break
    #     if flag:
    #         break
    # if flag:   
    #     count2=0
    #     for i in range(n):
    #         for j in range(n):
    #             if i!=j:
    #                 if mat[i][j]==i*n+(j+1):
    #                     # temp=mat[i][j]
    #                     # mat[i][j]=mat[j][i]
    #                     # mat[j][i]=temp
    #                     count+=1
    #                 else:
    #                     count2+=1
        
    #     print(count2)
    #     print(count//2 +1)
    # else:
    #     print(count)


    check=[-math.inf]*n        
    i=0
    for j in range(n):
        if mat[i][j]!=i*n+(j+1):
            check[j]=1
        else:
            check[j]=0
    check.pop(0)
    # print(check)
    
    # if len(set(check))==1:
    #     if 1 in set(check):
    #         print(1)
    #     else:
    #         print(0)
    # else:
    #     if check[0]==1 and check[1]==0 and check[2]==0:
    #         print(1)
    #     elif check[0]==1 and check[1]==1 and check[2]==0:
    #         print(1)
    #     elif check[0]==1 and check[1]==0 and check[2]==1:
    #         print(3)
    #     elif check[0]==0 and check[1]==0 and check[2]==1:
    #         print(2)
    #     elif check[0]==0 and check[1]==1 and check[2]==0:
    #         print(2)
    #     elif check[0]==0 and check[1]==1 and check[2]==1:
    #         print(2)
    



    count=0
    for i in reversed(range(0,len(check))):
        
        if check[i]==1:
            count+=1
            for j in range(0,i+1):
                if check[j]==0:
                    check[j]=1
                else:
                    check[j]=0
    
    print(count)

    
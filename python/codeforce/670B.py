for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    # if n==5:
    #     ans=1
    #     for num in a:
    #         ans*=num
    #     print(ans)
    # else:
    ans=list()
    a.sort()
    count=0

    for i in range(n-5,n):
        mul1=1
        for k in range(i,n):
            mul1*=a[k]
                    
        for j in range(0,count):
            mul1*=a[j]
        count+=1
        ans.append(mul1)
    
    print(max(ans))

    
    










            
        
                

            



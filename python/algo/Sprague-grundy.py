def calculatemex(Set):
    m=0
    while m in Set:
        m+=1
    return m

def calculategrundy(n,dp):
    dp[0]=0
    dp[1]=1
    dp[2]=2
    dp[3]=3

    if dp[n]!=-1:
        return dp[n]

    Set=set()
    
    for i in range(1,3):
        Set.add(calculategrundy(n-i,dp))
    
    dp[n]=calculatemex(Set)

    return dp[n]

def declarewinner(a,dp,n):
    xorvalue=dp[a[0]]
    for i in range(1,n):
        xorvalue=xorvalue^dp[a[i]]
    
    if xorvalue!=0:
        print("win")
    else:
        print("lose")



for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mm=max(a)
    dp=[-1]*(mm+1)

    for num in a:
        calculategrundy(num,dp)
    
    declarewinner(a,dp,n)
    

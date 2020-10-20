def calulatemex(Set):
    m=0
    while m in Set:
        m+=1
    
    return m

def calculategrundy(n,dp):
    if n==0:
        return 0
    
    if dp[n]!=-1:
        return dp[n]
    
    Set=set()
    Set.add(calculategrundy(n//2,dp))
    Set.add(calculategrundy(n//3,dp))
    Set.add(calculategrundy(n//6,dp))

    dp[n]=calulatemex(Set)

    return dp[n]


for _ in range(int(input())):
    n=int(input())
    dp=[-1]*(n+1)
    print(calculategrundy(n,dp))
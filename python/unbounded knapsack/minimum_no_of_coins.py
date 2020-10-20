import sys
def minimumNoOfCoin(coin,sum,n):
    t=[[0 for j in range(sum+1)]for i in range(n+1)]
    for i in range(sum+1):
        t[0][i]= sys.maxsize-1

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if coin[i-1]<=sum:
                t[i][j]= min( t[i][j-coin[i-1]]+1 , t[i-1][j] )
            else:
                t[i][j]= t[i-1][j]
    return t[n][sum]
coin=[1,2,3]
n=len(coin)
sum=5
print(minimumNoOfCoin(coin,sum,n))
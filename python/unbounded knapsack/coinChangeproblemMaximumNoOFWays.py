def maxcoinchange(coin,N):
    size=len(coin)
    t=[[0 for j in range(N+1)]for i in range(size+1)]
    for i in range(size + 1):
        t[i][0] = 1

    for i in range (1,size+1):
        for j in range(1,N+1):
            if j>=coin[i-1]:
                t[i][j] = t[i-1][j] + t[i][j-coin[i-1]]

            else:
                t[i][j]= t[i-1][j]
    return t[size][N]

coin=[1,2,3]
N=4
print(maxcoinchange(coin,N))
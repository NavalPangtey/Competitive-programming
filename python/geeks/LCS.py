def LCS(a,b,n,m):
    lcs=[[0 for i in range(m+1)]for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                lcs[i][j]=lcs[i-1][j-1]+1
            else:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])

    return lcs[n][m]

a=input()
b=input()
n=len(a)
m=len(b)

print(LCS(a,b,n,m))
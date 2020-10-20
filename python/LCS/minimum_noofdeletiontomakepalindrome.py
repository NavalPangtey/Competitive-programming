def minNoofInsertionAndDeletion(x,y,n,m):
    t=[[0 for i in range(m+1)]for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+ t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])

    deletion= n-t[n][m]
    return deletion

x='agbcba'
y=x[::-1]
n=len(x)
m=len(y)
print(minNoofInsertionAndDeletion(x,y,n,m))
def LCS(x,y,n,m):
    t = ([[0 for i in range(m + 1)] for i in range(n + 1)])
    result=0
    for i in range(1,n+1):
        for j in range(1,m+1):

             if x[i-1]==y[j-1]:
                t[i][j]= t[i-1][j-1]+1
                result = max(result, t[i][j])
             else:
                t[i][j]= 0

    return result

x='pangteynavalS'
y='pangtey'
n=len(x)
m=len(y)
print(LCS(x,y,n,m))
def LCS(x,y,n,m):
    if n==0 or m==0:
        return 0
    if t[n][m]!=-1:
        return t[n][m]
    if x[n-1]==y[m-1]:
        t[n][m]=1+ LCS(x,y,n-1,m-1)
        return t[n][m]
    else:
        t[n][m]= max(LCS(x,y,n,m-1),LCS(x,y,n-1,m))
        return t[n][m]


x='naa'
y='nalsfg'
n=len(x)
m=len(y)
t=([[-1  for i in range(m+1) ]for i in range(n+1)])
print(t)
print(LCS(x,y,n,m))
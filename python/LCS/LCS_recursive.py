def LCS(x,y,n,m):
    if n==0 or m==0:
        return 0

    if x[n-1]==y[m-1]:
        return (1+ LCS(x,y,n-1,m-1))
    else:
        return max(LCS(x,y,n,m-1),LCS(x,y,n-1,m))


x='naasdfasfasfdvafgsefghgjuhgmfhdghdsfhsdghl'
y='nalsadfasfasfdhgdhdghghdbrgjuiyjhesrgwarhni'
n=len(x)
m=len(y)
print(LCS(x,y,n,m))
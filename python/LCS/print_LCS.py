def LCS(x,y,n,m):
    t = ([[0 for i in range(m + 1)] for i in range(n + 1)])
    for i in range(1,n+1):
        for j in range(1,m+1):

             if x[i-1]==y[j-1]:
                t[i][j]= t[i-1][j-1]+1
             else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])
    i=n
    j=m
    s=''
    while i>0 and j>0:
        if x[i-1]== y[j-1]:
            # s.append(x[i-1])
            s += str(x[i-1])
            i-=1
            j-=1
        else:
            if t[i][j-1]> t[i-1][j]:
                j-=1
            else:
                i-=1
    return s[::-1]





x='pangteysdfasf'
y='pangtey'
n=len(x)
m=len(y)
print(LCS(x,y,n,m))
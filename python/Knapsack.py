
def knapsack(wt,val, W,n):

      # if n==0 or W==0:    #base conditon
      #  return 0

    t=[[0 for x in range(W + 1)] for x in range(n + 1)]
    # for i in range(n+1):
    #     for j in range(W+1):
    #         if i==0 or j==0:
    #             t[i][j]=0

    # i,j=1,1

    for i in range(n+1):
         for j in range(W+1):
            if i == 0 or j == 0:
                 t[i][j] = 0
            elif(wt[i-1]<=j):
                t[i][j] = max(val[i - 1] + t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j]= t[i-1][j]

    return t[n][W]
    # if t[n][W]!=-1:
    #     return t[n][W]

    # if wt[n-1]<=W :
    #    t[n][W] = max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1), knapsack(wt, val, W, n - 1))
    #    return t[n][W]

    # elif(wt[n-1]>W):
    #    t[n][W] = knapsack(wt, val, W, n - 1)
    #    return t[n][W]



wt = [1,3,4,5,4,5,2,4,7,84,5]
val =[1,4,5,7,5,6,7,4,2,93,4]
n=11
W=7
# row=100
# colm=1002
# t= [[-1]*colm]*row
# t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

print(knapsack(wt,val,W,n))



import sys
def subsetsum(arr,n):
   sum2 =0
   sum2=sum(arr)
   t =([[0 for j in range(sum2 + 1)]for i in range(n + 1)])
   for i in range(n + 1):
       t[i][0] = True
   for i in range(1, sum2 + 1):
       t[0][i] = False

   for i in range(1,n + 1):
       for j in range(1,sum2 + 1):
           if j>=arr[i-1]:
               t[i][j]= (t[i-1][j-arr[i-1]] or t[i-1][j])
           else:
               t[i][j]= t[i-1][j]

   diff = 0  #sys.maxsize

   for j in range(sum2//2,-1,-1):#we ca also use reversed(range(sum2//2)) to revere an array
       if t[n][j]==True:
           diff= sum2-(2*j)
           break
   return diff

arr=[1, 6, 11, 5]
n=len(arr)
print(subsetsum(arr,n))
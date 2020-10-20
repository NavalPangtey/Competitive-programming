def subsetsum(arr,sum,n):
   t =([[0 for j in range(sum + 1)]for i in range(n + 1)])
   for i in range(n + 1):
       t[i][0] = 1
   for i in range(1, sum + 1):
       t[0][i] = 0

   for i in range(1,n + 1):
       for j in range(1,sum + 1):
           if j>=arr[i-1]:
               t[i][j]= (t[i-1][j-arr[i-1]] + t[i-1][j])
           else:
               t[i][j]= t[i-1][j]
   return t[n][sum]
arr=[1,1,2,3]
n=len(arr)
diff=1
sumarr=0
sumarr=sum(arr)
sum= (diff+sumarr)//2

print(subsetsum(arr,sum,n))

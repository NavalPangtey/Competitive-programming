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
arr=[2,3,5,6,8,10,0]
n=7
sum=10
print(subsetsum(arr,sum,n))


# The problem is, that initializing the entire column with 1 will work only if the input array has all non-zero elements.


# def find_zeros_in_array(arr):
#
# 	return len([x for x in arr if x==0])
#
#
#
# def count_of_subsets_with_given_sum_corrected(arr,n,W):
#
# 	K = [[0 for x in range(W+1)] for x in range(n+1)]
#
#
#
# 	for i in range(n+1):
#
# 		for j in range(W+1):
#
#
#
# 			if i==0 or j==0:
#
# 				if i==0: K[i][j] = 0
#
# 				if j==0: K[i][j] = 2**find_zeros_in_array(arr[:I])
#  #the only line that's different from the video
#
#
# 			elif arr[i-1]<=j:
#
# 				K[i][j] = K[i-1][j-arr[i-1]] + K[i-1][j]
#
#
#
# 			else:
#
# 				K[i][j] = K[i-1][j]
#
#
#
# 	return K[n][W]
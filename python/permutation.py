from itertools import permutations
#from random import randrange
# p =permutations([1,2,3])
# for i in list(p):
#     print(i)
#     break

t= int(input())
for i in range(t):
   n= map(int,input().split())
   L= list(map(int,input().split()))
   for k in range(n):
        p=k
        lp=n-p+1
        permutations(L)
        inc = all(i < j for i, j in zip(L, L[:p]))
        dec = all(i < j for i, j in zip(L, L[lp:]))

   if inc==true and dec==true:
       print('YES')
       lper=permutations(L)
       for i in list(lper):
           print(i)
           break
   else:
       print('NO')

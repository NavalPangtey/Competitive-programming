 # from itertools import permutations
 # L=[1,2,3,4,3,2,1]
 # for k in range(n)
 #        p=k
 #        lp=n-p+1
 #        permutations(L)
 #        return inc = all(i < j for i, j in zip(L, L[:p]))
 #        return dec = all(i < j for i, j in zip(L, L[lp:]))

# n=int(input())
# for p in range(n):
#     xx=int(input())
#     a=list(map(int,input().split()))
#     b=[]
#     flag=0
#     aa=a.copy()
#     aa.sort()
#     i=0
#     while(i<xx-2):
#         if(aa[len(aa)-1]==aa[len(aa)-2] or aa[i]==aa[i+2]):
#             flag=1
#         elif(aa[i]==aa[i+1]):
#             b.append(aa[i+1])
#             aa.pop(i+1)
#         xx=len(aa)
#         i+=1
#     b.sort(reverse=True)
#     if flag==0:
#         print('YES')
#         print(*aa,end=' ')
#         print(*b)
#     else:
#         print('NO')

n = int(input())

i=1
for i in range(10):
    print("{0}x{1}={2}",format(n,i,n*i))

# r=input()
# for i in range(r):
#     def arrangeCoins( n):
#       count=0
#       t=n
#       if(t==1):
#          return 1
#       elif(t==0):
#          return 0
#       else:
#           if(t>100000):
#              t=t/2
#           for i in range(t):
#               for k in range(i+1):
#                   count+=1
#                   if(count<=n):
#                      pass
#                   else:
#                      return i

def arrangeCoins(n):
  # left=0
  # right=n
  # lx=0
  # while(left<=right):
  #      mid = left + (right-left)/2
  #      if(mid*(mid+1)/2<=n):

  #          lx=mid
  #          left=mid+1

  #      else:
  #          right= mid-1

  # return lx
  left, right = 0, n
  while left <= right:
      k = (right + left) // 2
      curr = k * (k + 1) // 2
      if curr == n:
          return k
      if n < curr:
          right = k - 1
      else:
          left = k + 1
  return right

N= int(input())
print(arrangeCoins(N))



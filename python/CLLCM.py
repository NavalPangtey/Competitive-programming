def Print(n):
    if n==1:
      return n
    else:
      return n*Print(n-1)






n =int(input())
print(Print(n))

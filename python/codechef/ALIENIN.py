import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

o, x, n = input().split()
x = int(x)
l=list(n)
s1=''
s2=''
for i in range(len(l)):
    if i+1<=x:
        s1+=l[i]
    else:
        s2+=l[i]
if s1:
   s1=int(s1)
else:
    s1=0
if s2:
   s2=int(s2)
else:
    s2=0

if o=='-':
    print(s1-s2)
elif o=='+':
    print(s1+s2)
elif o=='/':
    print(s1/s2)
elif o=='*':
    print(s1*s2)


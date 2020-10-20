import math
def calculateMex(Set): 
    Mex = 0
  
    while (Mex in Set): 
        Mex += 1
  
    return (Mex) 
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    Set=set()
    Set2=set()
    for num in a:
        if num in Set:
            Set2.add(num)
        Set.add(num)
    
    A=calculateMex(Set)
    B=calculateMex(Set2)
    print(A+B)

    

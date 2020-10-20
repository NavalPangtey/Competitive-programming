
# prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223]
import math as mt
def largestFact(x):
    if x==1:
        return 1
    if x==2:
        return 1
    # for num in prime:
    #     if x==num:
    #         return 1
    #         break
    #     elif x%num==0:
    #         return x//num
    #         break
    # return 1
    #  flag=1
    #     for i in range(2, mt.ceil(mt.sqrt(M))+1):
    #         if (M%i==0):
    #             flag=0
    #             break
    #     if flag:
    #         L.append(1)
    #         M=1
    #     else:
    for i in reversed(range(1,(x//2)+1)):
        # print(i)
        if x%i==0:
            # print(i)
            x=i
            break

    return x

m=2
n=4
# m,n=map(int,input().split())
M=m
N=n
L=list()
if n==m:
    print(0)
else:
    while M!=1:
        flag=1
        for i in range(2, mt.ceil(mt.sqrt(M))+1):
            if (M%i==0):
                flag=0
                break
        if flag:
            L.append(1)
            M=1
        else:
            M=largestFact(M)
            L.append(M)
        

    while N!=1:
        flag2=1
        for i in range(2, mt.ceil(mt.sqrt(N))):
            if (N%i==0):
                flag2=0
                break
        if flag2:
            L.append(1)
            N=1
        else:
            N=largestFact(N)
            L.append(N)
        

    # print(L)
    L.sort()
    L.reverse()
    S=set(L)
    # print(L)
    hh=0
    # print(S)
    check= False
    dic={}
    for k in L:
        dic[k]=dic.get(k,0)+1
    for x in dic:
        if dic.get(x)>1 and x>1:
            check=True
            hh=x
            break
    # print(dic)
    # print(hh)
   
    if m in S:
        count=0
        for num in L:
            count+=1
            if num==m:
                break
        print(count)
    elif n in S:
        count=0
        for num in L:
            count+=1
            if num==n:
                break
        print(count)
    elif check:
        count=0
        for num in L:
            count+=1
            if num==hh:
                count+=1
                break
        print(count)
    else:
        print(len(L))
# temp=0
# for x in dic:
#     if dic.get(x)==1:
#         temp+=1

# print(temp+2)
        

        
       


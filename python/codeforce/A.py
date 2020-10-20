# for _ in range(int(input())):
#     n= int(input())
#     a=list(map(int,input().split()))

#     # for i in range(1,len(a)):
#     #     if 
#     ans=list()
#     k=0
#     h=0
#     flag=False
#     i=1
#     while i<len(a) :
#         if len(a)==2:
#             flag=True
#             if a[0]!=a[1]:
#                 print(1)
#             else:
#                 print(2)
#             break
#         elif a[i-1]!=a[i]:
#             k=a[i-1]+a[i]
#             a.insert(i+1,k)
#             a.pop(i-1)
#             a.pop(i-1)
#             # print(k)
#             # a.insert(i-1,k)
#             i=1   
            
#         else:
#             i+=1

     
#     if flag==False:
#         print(len(a))

for _ in range(int(input())):
    n= int(input())
    a=list(map(int,input().split()))
    
    h=set()
    flag=False
    h.add(a[0])
    for num in a:
        if num in h:
            pass
        else:
            flag=True
            break
    
    if flag:
        print(1)
    else:
        print(n)
            
# modulo=1000000007
# factorialTable=list()
# # factorialTable.append(1)
# # factorialTable.append(1)
# def factorial(n): 
#     if n < 0: 
#         return 0
#     elif n == 0 or n == 1: 
#         factorialTable.append(1)
#     else: 
#         fact = 1
#         while(n>1): 
#             fact *= n
#             n -= 1
#             factorialTable.append(fact)

# factorialTable=list()
# factorial(10)
# print(factorialTable)
# import sys
# sys.stdout = open("/home/nav/code/python/algo/test.txt", "w")
# F=[-1]*10001
# fact=1
# for i in range(0,10001):
#     if i==0:
#         F[i]=1
#     else:
#         fact=fact*i
#         F[i]=fact

# print(F)
# sys.stdout.close()
modulo=1000000007

def ncr(n,k):
    m=0
    if k==0:
        m=1
    if k==1:
        m=n
    if k>=2:
        num,dem,op1,op2=1,1,k,n
        while(op1>=1):
          
            num*=op2
           
            
            dem*=op1
          
            op1-=1
            op2-=1
        m=num//dem
    return m%modulo

print(ncr(9,9))

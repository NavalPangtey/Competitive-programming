ppp=list()
def SieveOfEratosthenes(n,a) :
    prime = [True for i in range(n+1)]

    p=2
    while p*p<=n:
        if prime[p]==True:
            for i in range(p*p, n+1,p):
                prime[i]=False
        p+=1

    for p in range(a,n+1):
        if prime[p] :
            ppp.append(p)
            



a=int(input())
b=int(input())
SieveOfEratosthenes(b,a)
# print(ppp)
n=len(ppp)
lower=(a/2)*(b/2)
upper=a*b
for i in range(n-1):
    for j in range(i+1,n):
        if ppp[i]*ppp[j]>=lower and ppp[i]*ppp[j]<=upper:
            print(f'{ppp[i]},{ppp[j]}')



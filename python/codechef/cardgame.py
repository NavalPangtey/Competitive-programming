N = 100001
factorialNumInverse = [None] * (N + 1) 
naturalNumInverse = [None] * (N + 1) 
fact = [None] * (N + 1) 
def InverseofNumber(p): 
    naturalNumInverse[0] = naturalNumInverse[1] = 1
    for i in range(2, N + 1, 1): 
        naturalNumInverse[i] = (naturalNumInverse[p % i] * (p - int(p / i)) % p) 
  

def InverseofFactorial(p): 
    factorialNumInverse[0] = factorialNumInverse[1] = 1
    for i in range(2, N + 1, 1): 
        factorialNumInverse[i] = (naturalNumInverse[i] *factorialNumInverse[i - 1]) % p 

def factorial(p): 
    fact[0] = 1
    for i in range(1, N + 1): 
        fact[i] = (fact[i - 1] * i) % p 

def ncr(N, R, p): 
    ans = ((fact[N] * factorialNumInverse[R])% p *factorialNumInverse[N - R])% p 
    return ans 

p=1000000007
InverseofNumber(p) 
InverseofFactorial(p) 
factorial(p)
for _ in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    mm=max(c)
    freq=0
    total=0
    for num in c:
        if num==mm:
            freq+=1
    
    if freq==n:
        # Nfact=F[n]
        if n%2==0:
            t2=n//2-1
            for h in range(t2+1):
                total+= ncr(n,h,p) #Nfact//(F[h]*F[n-h])
        else:
            t2=n//2
            for h in range(t2+1):
                total+= ncr(n,h,p)#Nfact//(F[h]*F[n-h])
        total=total*2
        print(total%p)
    else:
        k=n-freq
        # Kfact=F[k]
        for i in range(0,k+1):
            total+= ncr(k,i,p)#Kfact//(F[i]*F[k-i])
        total=(total*2)
        # print(total)
        total2=0
        # FreqFact=F[freq]
        if freq%2==0:
            t2=freq//2-1
            for h in range(1,t2+1):
                tt= ncr(freq,h,p)
                total2+=total*tt
        else:
            t2=freq//2
            for h in range(1,t2+1):
                tt= ncr(freq,h,p)#FreqFact//(F[h]*F[freq-h])
                total2+=total*tt
        total=total2+total
        print(total%p)












    
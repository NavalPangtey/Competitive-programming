def isPrime(y):
    i=2
    while i*i<y:
        if y%i==0:
            return 0
        i+=1
    return 1


def isSemiPrime(a):
    i=2
    while i*i<a:
        if  a%i==0 and isPrime(i) and isPrime(a/i) :
            return 1
        i+=1  
    return 0

def solve():
    n=int(input())
    for b in range(4,n//2):
        a=n-b
        if isSemiPrime(a) and isSemiPrime(b):
            print("YES")
            return
    print("NO")


for _ in range(int(input())):
    solve()
 
    
            

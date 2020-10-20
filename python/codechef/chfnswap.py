import math
for _ in range(int(input())):
    n=int(input())
    # for n in range(1,1000000000):
    sum=(n*(n+1))//2
    if sum%2==0:
        a=1
        b=1
        c=-sum
        r = b**2 - 4*a*c
        x1 = (((-b) + math.sqrt(r))/(2*a))     
        print(x1)
        s1=(int(x1)*(int(x1)+1))//2
        s2=sum-s1
        aa=n-int(x1)
        print(sum)
        print(aa)
        print(f'{s1} {s2}')
        # if s1==s2:
        #     ans=(int(x1)*(int(x1)-1))//2
        #     ans2=(aa*(aa-1))//2
        #     if ans2==1:
        #         ans2=0
        #     print(ans+ans2+aa)
         
        # else:
        #     print(aa)
        
    else:
        print(0)
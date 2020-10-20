import math
from math import ceil, floor, pow
def Round_off(N, n): 
    b = N 
    c = floor(N) 
    i = 0; 
    while(b >= 1): 
        b = b / 10
        i = i + 1
  
    d = n - i 
    b = N 
    b = b * pow(10, d) 
    e = b + 0.5
    if (float(e) == float(ceil(b))): 
        f = (ceil(b)) 
        h = f - 2
        if (h % 2 != 0): 
            e = e - 1
    j = floor(e) 
    m = pow(10, d) 
    j = j / m 
    return j

k=int(input())
if k==1:
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
            x1=int(x1)
            s1=(x1*(x1+1))//2
            s2=sum-s1
            aa=n-int(x1)
            if s1==s2:
                print(0)
                for i in range(n):
                    if i<x1:
                        print(1,end='')
                    else:
                        print(0,end='')
                print()
            
            else:
                print(0)
                s5=s2
                for i in range(x1+1,n+1):
                    s5=s2-i
                    s3=(sum//2)-s5
                    # print(i)
                    if s3<=x1:
                        l=i
                        break
                # print(f's3 {s3} s5 {s5}')
                ans=[1]*n
                for i in range(n):
                    if i<x1:
                        ans[i]=1
                    else:
                        ans[i]=0
                    
                    if i==s3-1 :
                        ans[i]=0
                    if i==l-1:
                        ans[i]=1
                
                for i in range(n):
                    print(ans[i],end="")
                print()
            
        else:
            print(1)
            a=1
            b=1
            c=-sum
            r = b**2 - 4*a*c
            x1 = (((-b) + math.sqrt(r))/(2*a))     
            x1=int(x1)
            s1=(x1*(x1+1))//2
            s2=sum-s1
            aa=n-int(x1)
            s9=((sum-1)//2)+1
            # print(x1)
            # print(f's1 {s1} s2 {s2} aa {aa}')
            if abs(s1-s2)==1:
                for i in range(n):
                    if i<x1:
                        print(1,end='')
                    else:
                        print(0,end='')
                print()
            else:
                s5=s2
                for i in range(x1+1,n+1):
                    s5=s2-i
                    s3=(s9)-s5
                    # print(i)
                    if s3<=x1:
                        l=i
                        break
                # print(f's3 {s3} s5 {s5}')
                ans=[1]*n
                for i in range(n):
                    if i<x1:
                        ans[i]=1
                    else:
                        ans[i]=0
                    
                    if i==s3-1 :
                        ans[i]=0
                    if i==l-1:
                        ans[i]=1
                
                for i in range(n):
                    print(ans[i],end="")
                print()

if k==2:
    for _ in range(int(input())):
        n=int(input())
        sum=(n * (n + 1) * ((2*n) + 1)) // 6
        print(sum)
        if sum%2==0:
            ss=0
            Set=set()
            for i in range(n):
                Set.add(i+1)
                ss+=(i+1)**2
                if ss>sum//2:
                    x1=i-1
                    break

            print(x1)
            s1=(x1 * (x1 + 1) * ((2*x1) + 1)) // 6
            s2=sum-s1
            aa=n-int(x1)
            print(f's1 {s1} s2 {s2}')
            
            if abs(s1-s2)<=2:
                print(abs(s1-s2))
                for i in range(n):
                    if i<x1:
                        print(1,end='')
                    else:
                        print(0,end='')
                print()
            
            else:
                s5=s2
             
                # for i in range(x1+1,n+1):
                s5=s2-(n**2)
                # if s5<sum//2:
                s3=abs((sum//2)-s5)
                # if math.sqrt(s3)<=x1 and math.sqrt(s3)>0:
                l=n
                    # break
                # print(f's3 {s3} s5 {s5}')
                print(s3)
                sss=int(s3)
                ss=str(sss)
                kkk=len(ss)
                roundofff=int(Round_off(math.sqrt(s3),kkk))
                ans=[1]*n
                for i in range(n):
                    if i<x1:
                        ans[i]=1
                    else:
                        ans[i]=0
                    if i==roundofff-1 :
                        ans[i]=0
                    if i==l-1:
                        ans[i]=1
                s2=s5+(roundofff**2)
                s1=s1-(roundofff**2)+(n**2)
                print(abs(s2-s1))
                for i in range(n):
                    print(ans[i],end="")
                print()
            
        # else:
        #     print(1)
        #     a=1
        #     b=1
        #     c=-sum
        #     r = b**2 - 4*a*c
        #     x1 = (((-b) + math.sqrt(r))/(2*a))     
        #     x1=int(x1)
        #     s1=(x1*(x1+1))//2
        #     s2=sum-s1
        #     aa=n-int(x1)
        #     s9=((sum-1)//2)+1
        #     # print(x1)
        #     # print(f's1 {s1} s2 {s2} aa {aa}')
        #     if abs(s1-s2)==1:
        #         for i in range(n):
        #             if i<x1:
        #                 print(1,end='')
        #             else:
        #                 print(0,end='')
        #         print()
        #     # else:
            #     s5=s2
            #     for i in range(x1+1,n+1):
            #         s5=s2-i
            #         s3=(s9)-s5
            #         # print(i)
            #         if s3<=x1:
            #             l=i
            #             break
            #     # print(f's3 {s3} s5 {s5}')
            #     ans=[1]*n
            #     for i in range(n):
            #         if i<x1:
            #             ans[i]=1
            #         else:
            #             ans[i]=0
                    
            #         if i==s3-1 :
            #             ans[i]=0
            #         if i==l-1:
            #             ans[i]=1
                
            #     for i in range(n):
            #         print(ans[i],end="")
            #     print()


            

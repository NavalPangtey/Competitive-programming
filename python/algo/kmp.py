def kmp(s,t,lps):
    
    n=len(s)
    m=len(t)
    count=[0 for x in range(n)]
    i=0
    j=0
    while i<n:
        count[i]=count[i-1]
        if t[j]==s[i]:
            i+=1
            j+=1
        if j==m:
            count[i-1]+=1
            j=lps[j-1]
        elif  i<n and t[j]!=s[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return count
            
            


def lpsa(t,m):
    l=0
    lps= [0 for i in range(m)]
    i=1
    while i<m:
        if t[i] ==t[l]:
            l+=1
            lps[i]=l
            i+=1
        else:
            if l!=0:
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1
    return lps
s=input()
t=input()
n=len(s)
m=len(t)
lps=lpsa(t,m)
one=kmp(s,t,lps)[-1]
count=kmp(s+s,t,lps)
two=count[-1]
three=two-(2*one)
for _ in range(int(input())):
    q=int(input())
    v=q//n
    if v:
        ans=v*one +(v-1)*three
        e=q%n
        ans+=count[n-1+e]-count[n-1]
    else:
        e=q%n
        ans=count[e-1]
    print(ans)
    # if one:
    #     if q>n:
    #         hh=q//n
    #         i=0
    #         for i in range(hh):
    #             ans+=one
    #     print(ans)
    # elif two:
    #     hh=q//(n+n)
    #     i=0
    #     for i in range(hh):
    #         ans+=two
    #     print(ans)
    # elif three:
    #     hh=q//(n+n+n)
    #     i=0
    #     for i in range(hh):
    #         ans+=three
    #     print(ans)
    # else:
    #     print(0)
    # S=''
    # if q<n:
    #     for i in range(q):
    #         S+=s[i]
    #     kmp(S,t,lps)
       
    # elif q==n:
    #     kmp(s,t,lps)
        
    # elif q%n==0:
    #     tt=q//n
    #     for i in range(tt):
    #         S+=s
    #     kmp(S,t,lps)
        
    # elif q%n!=0:
    #     temp=0
    #     while temp<q:
    #         temp+=n
    #     temp=temp-n
    #     tem=temp//n
    #     for i in range(tem):
    #         S+=s
          
    #     h=q-temp
    #     for i in range(h):
    #         S+=s[i]
    #     kmp(S,t,lps)
        


      



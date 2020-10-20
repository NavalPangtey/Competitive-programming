for _ in range(int(input())):
    n=int(input())
    s=''
    for i in range(n):
        t=input()
        s=s+t
    
    ss=list(s)
    dic={}
    for k in ss:
        dic[k]=dic.get(k,0)+1
    f= False
    for x in dic:
        if dic.get(x)!=n and dic.get(x)%n!=0:
            f=True
            break
    
    if f:
        print("NO")
    else:
        print("YES")

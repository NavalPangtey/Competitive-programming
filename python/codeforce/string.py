for _ in range(int(input())):
    n=int(input())
    s=input()
    c0=0
    c1=0
    for x in s:
        if x=='0':
            c0+=1
        else:
            c1+=1
    ans=''
    if c1==0 or c1<=n-1:
        for i in range(n):
            ans+='0'
        print(ans)
    elif c0==0 or c0<=n-1:
        for i in range(n):
            ans+='1'
        print(ans)
    else:
        for i in range(n):
            if i%2==0:
                ans+='1'
            else:
                ans+='0'
        print(ans)

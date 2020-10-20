for _ in range(int(input())):
    # n=input()
    n,k=map(int,input().split())
    s=input()
    c1=0
    c0=0
    for i in range(n):
        if s[i]=='0':
            c0+=1
        else:
            c1+=1
    
    numSeg=n//k
    
    if c1%numSeg or c0%numSeg:
        print("IMPOSSIBLE")
    else:
        c1=c1//numSeg
        c0=c0//numSeg
        ss=''
        for i in range(numSeg):
            if i%2==0:
                for i in range(c0):
                    ss+='0'
                for i in range(c1):
                    ss+='1'
            else:
                for i in range(c1):
                    ss+='1'
                for i in range(c0):
                    ss+='0'
        print(ss)

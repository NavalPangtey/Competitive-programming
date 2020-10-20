for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    a=list()
    zero=0
    one=0
    cc=int(s[0])
    change=0
    for ss in s:
        a.append(int(ss))
        if int(ss)!=cc:
            cc=~cc
            change+=1
    if change==0:
        print(0)
    elif k==n-1:
        print(0)
    else:
        if k>=change:
            print(0)
        else: 
            print(change-k)
    

    


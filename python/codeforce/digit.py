for _ in range(int(input())):
    n=int(input())
    s=input()
    a=list()
    for ss in s:
        a.append(int(ss))

    odd=0
    even=0
    for i in range(n):
        if (i+1)%2==0:
            if a[i]%2==0:
                even+=1
        else:
            if a[i]%2!=0:
                odd+=1
    if n%2==0:
        if even>0:
            print(2)
        else:
            print(1)
    else:
        if odd>0:
            print(1)
        else:
            print(2)

    
def modify(a):
    n= len(a)-1
    no_of_zero=0
    for i in range(n+1):
        if a[i]==0:
            no_of_zero+=1

    new_range=n+no_of_zero
    i=n
    for j in range(new_range,-1,-1):
        if a[i]==0:
            a[j]=a[i]
            a[j-1]=a[i]
        else:
            a[j]=a[i]
        i-=1
    print(a)


a=[1,2,3,0,1,1,0]

modify(a)
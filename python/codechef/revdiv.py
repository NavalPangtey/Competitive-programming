for _ in range(int(input())):
    n=int(input())
    nn=n
    l=0
    arr=list()
    arr.append(n)
    while nn:
        nn=nn//10
        l+=1
        arr.append(nn)
    arr.remove(0)
    if n==0:
        print('No')
    else:
        fl=False
        for i in range(1,l+1):
            if arr[i-1]%i!=0:
                fl=True
                break
        if fl:
            print('No')
        else:
            print("Yes")

     

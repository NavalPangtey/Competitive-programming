for _ in range(int(input())):
    n= int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            abin = bin(a[i]).replace("0b", "")
            bbin = bin(a[j]).replace("0b", "")
            aa=int(abin,2)
            bb=int(bbin,2)
            bbb=aa&bb

            if bbb==a[i]:
                count+=1
    
    print(count)

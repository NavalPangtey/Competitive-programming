
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    fl=False    
    for i in range(n):
        for j in range(i+1,n):
           
            if a[i]+a[j]==k:
                print(f'{i+1} {j+1}')
                fl=True
                break
        if fl==True:
            break
    if fl==False:
        print('NA')


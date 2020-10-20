def nimsum(a,n):
    nims=a[0]
    for i in range(1,n):
        nims=nims^a[i]
    print(f'xor={nims}')
    return nims

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    nimsum(a,n)
    sum=0
    for i in range(n):
        sum+=a[i]
    print(f'sum={sum}')

    # if nimsum(a,n)!=0:
    #     print('win')
    # else:
    #     print("lose")
    for j in range(1,int(input())):
        sum2=0
        for t in range(n):
            sum2+=j^a[t]
        binary=bin(sum2).replace("0b", "")
        print(f"sum for k= {j} :{sum2} {binary}")
    

   
    # And(ee,18)


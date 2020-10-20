for _ in range(int(input())):
    H,P= map(int,input().split())

    if P>=H:
        print(1)
        continue

    while P:
        H=H-P
        P=P//2
        
    
    if P<H:
        print(0)
    else:
        print(1)
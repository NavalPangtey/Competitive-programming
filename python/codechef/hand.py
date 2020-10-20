for _ in range(int(input())): 
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a.reverse()
    p11=0
    p22=0
    if n==1:
        print("first")
        
    elif n==2:
        if a[1]>a[0]:
            print("second")
         
        elif a[0]>a[1]:
            print("first")
           
        elif a[0]==a[1]:
            print("draw")
        
    elif n==3:
        p11=a[0]
        p22=a[1]+a[2]
        if p11>p22:
            print("first")
           
        elif p11==p22:
            print("draw")
           
        else:
            print("second")
            
    else:
        p11=a[0]
        p22=a[1]+a[2]

        for i in range(3,n):
            if i%2==0:
                p22+=a[i]
            else:
                p11+=a[i]
                
        if p11>p22:
            print("first")
        
        elif p11==p22:
            print("draw")
            
        else:
            print("second")
            
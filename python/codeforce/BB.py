for _ in range(int(input())):
    x1,y1,z1=map(int,input().split())
    x2,y2,z2=map(int,input().split())
    
    sum=0
    temp=0

    temp=min(z1,y2)
    sum=temp*2
    
    z1=z1-temp
    
    if z2:
        z2=z2-z1
    
    if z2:
        temp=min(z2,x1)
        z2=z2-temp
    
    if z2:
        temp=min(z2,y1)*2
        sum=sum-temp
    
    print(sum)



        

    

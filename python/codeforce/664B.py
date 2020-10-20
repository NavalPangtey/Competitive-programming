n,m,x,y=map(int,input().split())
k=y
while k>0:
    print(f"{x} {k}") 
    k-=1

flag=False
i=x
j=y+1
turn=1
while i<=n and i>0:
    if turn==1 or turn%2!=0:
        if turn>1:
            j=1
        while j<m+1:
            print(f"{i} {j}")
            j+=1
        turn+=1
    elif turn%2==0:
        j=m
        while j>0:
            print(f"{i} {j}")
            j-=1

        turn+=1
    if flag==False:
        i+=1
    if i==n+1:
        flag =True
        i=x-1  
    elif flag:
        i-=1
       
        



    
    
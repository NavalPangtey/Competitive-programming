for _ in range(int(input())): 
    n=str(input())
    a=list(n)
    # print(a)
    c=list()
    flag=False
    count=0
    for i in range(len(a)):
        if a[i]=='1':
            count+=1
            flag=True
        elif a[i]=='0' and flag==True :
            # print(count)
            c.append(count)
            count=0

        if i==len(a)-1 and a[i]=='1':
            c.append(count)
            
        
    c.sort()
    c.reverse()
    # print(c)
    ans=0
    for i in range(len(c)):
        if i==1:
            pass
        elif i%2==0 or i==0:
            ans+=c[i]
    
    print(ans)
       
            


for _ in range(int(input())):

    s=input()
    x=int(input())
    w=[]
    w=[-1]*len(s)
    n=len(s)
    flag=False
    for i in range(n):
        if s[i]=='0':
            if i-x>=0:       
                w[i-x]=0
         
            if i+x<=n-1:
                w[i+x]=0
               
                   
    for i in range(n): 
        if s[i]=='1':
            if i-x>=0:
                if w[i-x]==0:
                    if i+x<n:
                        if w[i+x]==0:
                            flag=True
                            break
                    else:
                        flag=True
                        break
            elif i+x<n:
                 if w[i+x]==0:
                    flag=True
                    break
            else:
                flag=True
                break
           
    
    
    if flag:
        print(-1)
    else:
        for i in range(n):
            if w[i]==-1:
                w[i]=1
            print(w[i],end='')
        print()

    


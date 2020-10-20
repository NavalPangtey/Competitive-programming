for _ in range(int(input())):
    N,K= map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    count2=0
    dic={}
    repeat=set()
    for k in a:
        dic[k]=dic.get(k,0)+1
    
    for x in dic:
        if dic.get(x)>1:
            count+=dic.get(x)
            count2+=1
            repeat.add(x)
   


    #**********************
    print(dic)
    #********************
    
    
    
    comes=set()
    coco=0
    for i in range(N):         
        if a[i] in repeat and a[i] not in comes:
            comes.add(a[i])
        elif a[i] in comes:
            coco+=1
            comes=set()
            comes.add(a[i])
        
        if i==N-1:
            if comes:
                coco+=1
    
    
    
    #********************
    print(coco)
    print(count)
    #********************
   
   
   
    if K==1:
        print(coco)
    else:
        if count2>1:
            if coco:     
                if coco*K>=count+K:
                    print(count+K)
                else:
                    print(coco*K)
            else:
                print(K) 
        else:
            print(count+K)                                                          

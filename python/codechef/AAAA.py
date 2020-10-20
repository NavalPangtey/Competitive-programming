for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    dic={}
    dic2={}
    for k in a:
        dic[k]=dic.get(k,0)+1
    
    b=set(a)
    d=list(b)
    temp=set()
    for x in dic:
        feq=dic.get(x)
        if feq not in temp:
            temp.add(feq)
            count=0
            for y in dic:
                if feq==dic.get(y):
                    count+=1
                dic2[feq]=count

    kk = list(dic2.values())
    
    kkk=max(kk)
    ans=[]

    for x in dic2:
        if dic2.get(x)==kkk:
            ans.append(x)

    print(min(ans))

                
        
            
        
            
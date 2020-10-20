for _ in range(int(input())):
    S=str(input())
    P=str(input())
    s=list(S) 
    p=list(P) 
    pp=p
    dic= {}
    for k in s:
        dic[k]=dic.get(k,0)+1
    
    dic2= {}
    for k in p:
        dic2[k]=dic2.get(k,0)+1
    print(dic)
    print(dic2)

    for x in dic2:
        if x in dic:
            dic[x]= dic.get(x)-dic2.get(x)

    print('********************')

    print(dic)
    s=[]
    for y in dic:
        rr=dic.get(y)
        while rr:
            s.append(y)
            rr-=1
    print(s)





    # s.sort()
    # Pset=set(p)
    # print(s)
    # for str2 in s:
    #     if str2 in Pset:
    #         s.remove(str2)
    #         pp.remove(str2)
    #         Pset=set(pp)
    
    # print(pp)
    # print(s)
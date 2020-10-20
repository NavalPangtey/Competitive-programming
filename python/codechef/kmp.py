
for _ in range(int(input())):
    S=str(input())
    P=str(input())
    s=list(S) 
    p=list(P) 
    increasing=0
    decreasing=0
    s.sort()
    if len(P)==1:
        ss=''.join(map(str, s))
        print(ss)
        continue
    
    # for str1 in p:
    #     for str2 in s:
    #         if str1==str2:
    #             s.remove(str2)
    #             break
    
    dic= {}
    for k in s:
        dic[k]=dic.get(k,0)+1
    
    dic2= {}
    for k in p:
        dic2[k]=dic2.get(k,0)+1
 

    for x in dic2:
        if x in dic:
            dic[x]= dic.get(x)-dic2.get(x)

    s=[]
    for y in dic:
        rr=dic.get(y)
        while rr:
            s.append(y)
            rr-=1
 
    # for str1 in p:
    #     s.remove(str1)
    
    for i in range(1,len(p)):
        if p[i-1]<=p[i]:
            if p[i-1]<p[i]:
                increasing=1
                break
            elif p[i-1]>p[i]:
                decreasing=1
                break
        else:
            decreasing=1
            break


    for i in range(len(s)):       
        if increasing:
            if s[i]>p[0]:
                s.insert(i,P)
                break
            elif i==len(s)-1:
                s.append(P)
                break
        else:
            if s[i]>=p[0]:
                s.insert(i,P)
                break
            elif i==len(s)-1:
                s.append(P)
                break

    if s:
        ans=''.join(map(str, s))
        print(ans)
    else:
        print(P)



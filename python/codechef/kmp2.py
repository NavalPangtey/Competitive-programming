for _ in range(int(input())):
    S=str(input())
    P=str(input())
    s=list(S) 
    p=list(P) 
    
    dic= {}
    for k in s:
        dic[k]=dic.get(k,0)+1
    
    
    pp=p
    increasing=0
    decreasing=0
    s.sort()
    if len(P)==1:
        ss=''.join(map(str, s))
        print(ss)
        continue
    Pset=set(pp)
    # for str1 in p:
    for str2 in s:
        if str2 in Pset:
            s.remove(str2)
            pp.remove(str2)
            Pset=set(pp)
            
    p=list(P)
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



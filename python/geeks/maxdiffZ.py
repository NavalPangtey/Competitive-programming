for i in range(int(input())):
    s=input()
    flag=False
    O=0
    Otemp=0
    Z=0

    ans=list()
    for i in range(len(s)):
        if s[i]=="0":
            Z+=1
            flag=True
            O+=Otemp
            Otemp=0
            if i==(len(s)-1):
                ans.append(Z-O)
            
            
        elif flag :
            Otemp+=1
            ans.append(Z-O)

        

      

    if Z>0:
        print(max(ans))
    else:
        print(-1)
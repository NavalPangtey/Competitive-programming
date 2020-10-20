import collections
for _ in range(int(input())):
    n,s=map(str,input().split())
    s=int(s)
    nn=list(n)

    for i in range(len(nn)):
        nn[i]=int(nn[i])
 
    if sum(nn)<=s:
        print(0)
    else:
        S=s
        li=list()
        if nn[0]>=s:
            ans=10**len(nn)
            print(ans-int(n))
        else:
            for i in range(len(nn)):
                if nn[i]<=S:
                    S=S-nn[i]
                else:
                    nn[i-1]=nn[i-1]+1
                    for j in range(i,len(nn)):
                        nn[j]=0
                    
                    break
            h=''
            for i in range(len(nn)):
                h+=str(nn[i])
            h+='0'
            print(int(h)-int(n))

                



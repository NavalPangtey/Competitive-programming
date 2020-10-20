ans=[]
t=int(input())
for _ in range(t):
    n,k=map(int, input().split())
    a=list(map(str,input().split()))
    count=0
    t=n-k
    for i in reversed(range(t,n)) :
        if a[i]=='T':
            a.pop()
        else:
            a.pop()
            for j in range(len(a)):
                if a[j]=="H":
                    a[j]='T'
                else:
                    a[j]='H'
    
    for i in range(len(a)):
        if a[i]=='H':
            count+=1

    ans.append(count)
        
for i in range(len(ans)):
    print(ans[i])
import sys
max = sys.maxsize
for _ in range(int(input())):
    N,K= map(int,input().split())
    p=list(map(int,input().split()))
    jj=0
    jk=0
    ans=[]
    for i in range(N):
        if K%p[i]==0:
            jk=(K//p[i])-1
            ans.append(jk)
        else:
            ans.append(max)
    tt=min(ans)
    if tt==max:
        print(-1)
    else:

        for i in range(N):
            if ans[i]==tt:
                print(p[i])







    # if jj:
    #     print(jj)
    # else:
    #     print(-1)
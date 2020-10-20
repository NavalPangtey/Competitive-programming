for j in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=0
    count=0
    ans=list()
    diff=a[0]-a[1]
    i=1
    while i<n:    
        t=a[i-1]- a[i]
        ans.append(t)
        i+=1
        # if t==diff:
        #     count+=1
        #     i+=1
        # else:
        #     ans.append(count)
        #     count=0
        #     diff=t
    max=-1
    count=0
    prev=ans[0]
    i=0
    while i<len(ans):
        if ans[i]==prev:
            count+=1
            i+=1
            if max<count:
                max=count
        else:   
            count=0
            prev=ans[i]
         
    print("Case #{}: {}".format(j+1,max+1))
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    maxi=-1
    ans=[]
    for num in a:
        if num==0:
            count+=1
        else:
            ans.append(count)
       
            count=0

    maxi= max(ans)

    if maxi%2==0:
        print('No')
    elif len(ans)==1 and maxi%2!=0:
        print("Yes")
    else:
        ans.sort()
        m1=ans[-1]
        m2=ans[-2]
        if m2>=(m1//2)+1:
            print("No")
        else:
            print('Yes')









  

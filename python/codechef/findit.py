import sys
def get_ints(): 
    return list(map(int, sys.stdin.readline().strip().split()))
for _ in range(int(input())):
    n=int(input())
    a=get_ints()
    Set=set()
    Set2=set()
    ans=0
    for num in a:
        if num in Set:
            Set2.add(num)
        Set.add(num)
    d=list(Set2)
    for num in d:
        fl=False
        for j in range(n):
            if a[j]==num:
                if fl:
                    mm=l2
                    if mm[0]%2==0:
                        te=0
                        sum=0
                        for j in range(1,len(mm)):
                            if mm[j]%2==0:
                                te+=1
                            sum+=mm[j]
                        if te%2==0:
                            if sum>ans:
                                ans=sum
                            
                    else:
                        te=0
                        sum=0
                        for j in range(1,len(mm)):
                            if mm[j]%2!=0:
                                te+=1
                            sum+=mm[j]
                        if te%2!=0:
                            if sum>ans:
                                ans=sum
                l2=list()
                fl=True
            if fl:
                l2.append(a[j])
       

    
    print(ans)
        
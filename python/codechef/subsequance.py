b=list()
M = 1000000007
def Subsequences(arr, index, subarr): 
     
    if index == len(arr): 
        if len(subarr) != 0: 
            print(subarr)
            temparr=subarr
            dic={}
            for k in temparr:
                dic[k]=dic.get(k,0)+1
            maxm=0
            maxy=0
            for x in dic: 
                maxm=dic.get(x)    
                if maxm>maxy:
                    maxy=maxm
                    MM=x
            gg=0
            for x in dic:
                if maxy==dic.get(x):
                    gg+=1
                    if gg>2:
                        break
            samllest=set()
            if gg>=2:
                for x in dic:
                    if maxy==dic.get(x):
                        samllest.add(x)
                
                MM=min(samllest)
                    
            
            b.append(MM)
            
      
    else: 
        Subsequences(arr, index + 1, subarr) 

        Subsequences(arr, index + 1,subarr+[arr[index]]) 
      
    return
          
for _ in range(int(input())):
    N= int(input())
    arr=list(map(int,input().split()))
    help=set(arr)
    Subsequences(arr, 0, []) 
    dic2= {}
    
    # for k in b:
    #     dic2[k]=dic2.get(k,0)+1
    total=0
    for i in range(1,N+1):
        if i in help:
            for num in b:
                if num==i:
                    total+=1
            total=total%M
            dic2[i]=total
            total=0


    ans=list()
    for i in range(1,N+1):
        if i in dic2:
            # crr=dic2.get(i)
            ans.append(dic2.get(i))
        else:
            ans.append(0)
    for i in range(N):
        print(ans[i],end=' ')
    print()
    b=list()
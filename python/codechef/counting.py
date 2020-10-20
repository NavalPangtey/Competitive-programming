b=list()

def SubArrays(arr, start, end):      
    if end == len(arr): 
        return
    elif start > end: 
        return SubArrays(arr, 0, end + 1)  
    else: 
        # print(arr[start:end + 1]) 
        temparr=arr[start:end + 1]
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
        b.append(MM)


        return SubArrays(arr, start + 1, end) 

for _ in range(int(input())):
    N= int(input())
    a=list(map(int,input().split()))
    SubArrays(a, 0,[])

    print(b)
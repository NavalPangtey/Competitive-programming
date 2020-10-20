import math
import itertools

def seq(start, end, step):
    if step == 0:
        raise ValueError("step must not be 0")
    sample_count = int(abs(end - start) / step)
    return itertools.islice(itertools.count(start, step), sample_count)
for _ in range(int(input())):
    n=int(input())
    v=list(map(int,input().split()))
    mat=[]
    # for j in range(5):
    for j in seq(0,5, 0.01):
        gg=[-1]*n
        for i in range(n):
            g=(i+1)+(v[i]*j)
            gg[i]=round(g)
        mat.append(gg)
     
    # for i in range(300):
    #     for j in range(n)  :
    #         print(mat[i][j],end=' ')
    #     print()
    ans=list()   
    for k in range(1,n+1):
        Set =set()
        Set.add(k)
        # for i in range(5):
        for i in range(500):
            for j in range(n):
                if j+1 not in Set:
                    lis1=list()
                    lis2=list()
                    lis1=list(Set)
                    lis2=lis1[:]
                    # print(lis2)
                    for b in lis2:
                        if mat[i][j]==mat[i][b-1]:  
                            Set.add(j+1)
        
        print(Set)
        ans.append(len(Set))
    print(f'{min(ans)} {max(ans)}')

   

   
   
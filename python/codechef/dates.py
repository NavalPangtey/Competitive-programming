import math
mat=[]
n=int(input())
for i in range(n):
    s=input()
    dd=''
    date=list()
    for ss in s:
        if ss=='/':
            date.append(int(dd))
            dd=''
        else:
            dd+=ss
    date.append(int(dd))
    mat.append(date)

    

for i in range(n):
    minYear=math.inf
    for j in range(n):
        if mat[j][2]<minYear:
            minYear=mat[j][2]
    
    minMounth=math.inf
    for j in range(n):
        if mat[j][1]<minMounth and mat[j][2]==minYear:
            minMounth=mat[j][1]

    minDate=math.inf
    for j in range(n):
        if mat[j][0]<minDate and mat[j][2]==minYear and mat[j][1]==minMounth:
            minDate=mat[j][0]
    
    print(f'{minDate}/{minMounth}/{minYear}')

    for j in range(n):
        if mat[j][0]==minDate and mat[j][1]==minMounth and mat[j][2]==minYear:
            mat[j][0]=math.inf
            mat[j][1]=math.inf
            mat[j][2]=math.inf
            break





try :
    for i in range(int(input())):

        n = int(input())
        pt1=0
        pt2=0
        r=2
        y=0
        u=1
        A=0
        B=0

        for j in range(n):
            #A=str(raw_input())
            #B=str(raw_input())
            AF=list(map(int, input().split()))
            A=AF[0]
            B=AF[1]
            flag=1
            a = list(map(int, str(A)))
            b = list(map(int, str(B)))
            at=sum(a)
            bt=sum(b)
            if at>bt:
                pt1+=1
            elif bt>at:
                pt2+=1
            else:
                pt1+=1
                pt2+=1


        if(pt1==pt2):
            print('{} {}'.format(r,pt2))
        elif(pt1>pt2) :
            print('{} {}'.format(y,pt1))
        elif(pt2>pt1):
            print('{} {}'.format(u,pt2))
except Exception:
    pass













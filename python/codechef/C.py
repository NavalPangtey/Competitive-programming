import sys
for _ in range(int(sys.stdin.readline().strip())):
    s=input()
    a=list(s)
    x1,y1= map(int, sys.stdin.readline().strip().split())

    dic= {}
    for k in a:
        dic[k]=dic.get(k,0)+1
    
    # R,L,U,D=0,0,0,0
    # for x in s:
    #     if x =="R":
    #         R+=1
    #     elif x=="L":
    #         L+=1
    #     elif x=="U":
    #         U+=1
    #     elif x=="D":
    #         D+=1
    
    # xmax=x1+R
    # xmin=x1-L
    # ymax=y1+U
    # ymin=y1-D


    for _ in range(int(sys.stdin.readline().strip())):
        x2,y2=map(int, sys.stdin.readline().strip().split())
        
       
        # checkA=False
        # checkB=False

        # if x2<=xmax and x2>=xmin:
        #     checkA=True
        
        # if y2<=ymax and y2>=ymin:
        #     checkB=True
    

        xx=abs(x2-x1)
        yy=abs(y2-y1)



        # R=False
        # L=False
        # U=False
        # D=False
        # dic= {}
        # checkA=False
        # checkB=False
        # for k in a:
           
        #     dic[k]=dic.get(k,0)+1
        #     if k=="R" and dic[k]>=xx:
        #         R=True
        #     if k=="L" and dic[k]>=xx:
        #         L=True
            
        #     if k=="U" and dic[k]>=yy:
        #         U=True
            
        #     if k=="D" and dic[k]>=yy:
        #         D=True
            
        #     if x2>x1:
        #         if R:
        #             checkA=True
        #     elif x2<x1:
        #         if L:
        #             checkA=True
        #     elif x2==x1:
        #         checkA=True

        #     if y2>y1:
        #         if U:
        #             checkB=True
        #     elif y2<y1:
        #         if D:
        #             checkB=True
        #     elif y2==y1:
        #         checkB=True
            

        #     if checkA and checkB:
        #         break



        # flag1=False
        # flag2=False

        # if x2>x1:
        #      if R:
        #         flag1=True
        # elif x2<x1:
        #      if L:
        #         flag1=True
        # elif x2==x1:
        #     flag1=True


        # if y2>y1:
        #      if U:
        #          flag2=True
        # elif y2<y1:
        #      if D:
        #          flag2=True
        # elif y2==y1:
        #     flag2=True
                 
       
        if x2>x1:
            count=0
            for i in range(len(a)):
                if a[i]=='R':
                    count+=1
                   
                
                if count==xx:
                    flag1=True
                    break
                   
        elif x2<x1:
            count=0
            for i in range(len(a)):
                if a[i]=='L':
                    count+=1
                
                if count==xx:
                    flag1=True
                    break
        elif x2==x1:
            flag1=True

        if y2>y1:
            count1=0
            for i in range(len(a)):
                if a[i]=='U':
                    count1+=1
                
                if count1==yy:
                    flag2=True
                    break
                    
        elif y2<y1:
            count1=0
            for i in range(len(a)):
                if a[i]=='D':
                    count1+=1
                
                if count1==yy:
                    flag2=True
                    break
        elif y2==y1:
            flag2=True

        # if checkA and checkB:
        #     print(f"YES {xx+yy}")
        # else:
        #     print("NO")


        if flag1 and flag2:
            print(f"YES {xx+yy}")
        else:
            print("NO")


            
            


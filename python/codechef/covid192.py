import math
for _ in range(int(input())):
    n=int(input())
    if n==3:
        v=list(map(int,input().split()))
        mat=[]
        for j in range(1,21):
            t=[-1]*n
            for i in range(n):
                if j==1:
                    if v[0]==0:
                        t[0]=0
                elif j==2:
                    if i==0:
                        if v[i]!=0:
                            t[0]=(j-(i+1))/v[i]
                        else:
                            t[0]=-1
                    elif i==1:
                        if v[i]==0:
                            t[1]=0

                elif j==3:
                    if i==0:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==1:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==2:
                        if v[i]==0:
                            t[i]=0
                
                else:

                    if v[i]!=0:
                        t[i]=(j-(i+1))/v[i]
                    else:
                        t[i]=-1

            mat.append(t)
        # for i in range(20):
        #     for j in range(n)  :
        #         print(mat[i][j],end=' ')
        #     print()
        
        # if sum(t)!=0:
        # ans=list()   

        A=[-1]*(20)
        B=[-1]*(20)
        C=[-1]*(20)
        for b in range(n):
            # Set.add(b)

            for i in range(20):
                
                # if j+1 not in Set:
                # lis1=list()
                Set=set()
                # lis2=list()
                # lis1=list(Set)
                # lis2=lis1[:]

                for j in range(0,b):
                    if mat[i][j]>0 and mat[i][b]==0:
                        Set.add(j)
                    elif mat[i][j]>mat[i][b] or mat[i][j]==0 or mat[i][j]==-1 or mat[i][b]==-1:
                        pass
                    else:
                        Set.add(j)
                
                    
                for j in range(b+1,n):
                    if mat[i][j]==0  and mat[i][b]> 0:                    
                        Set.add(j)
                    elif mat[i][j]<mat[i][b]   or mat[i][b]==0 or mat[i][j]==-1 or mat[i][b]==-1 :
                        pass
                    else:
                        Set.add(j)
                lis1=list(Set)
                if b==0:
                    A[i]=lis1
                elif b==1:
                    B[i]=lis1
                elif b==2:
                    C[i]=lis1
            # print(Set)
            # ans.append(len(Set))
        
        size1=A[0]
        for i in range(len(A)):
            if len(A[i])!=0:
                if A[i]!=size1:
                    size1=A[i]
                else:
                    A[i]=[]
        size2=B[0]
        for i in range(len(B)):
            if len(B[i])!=0:
                if B[i]!=size2:
                    size2=B[i]
                else:
                    B[i]=[]
        size3=C[0]
        for i in range(len(C)):
            if len(C[i])!=0: 
                if C[i]!=size3:
                    size3=C[i]
                else:
                    C[i]=[]


        # print(A)
        # print(B)
        # print(C)


        AA=set()
        for i in range(len(A)):
            if len(A[i])>0:
                aa=A[i]
                for t in aa:
                    AA.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==1:
                        for k in range(i+1,20):
                            gg=B[k]
                            for t in gg:
                                AA.add(t)
                    if aa[j]==2:
                        for k in range(i+1,20):
                            gg=C[k]
                            for t in gg:
                                AA.add(t)

        # print(AA)
        BB=set()
        for i in range(len(B)):
            if len(B[i])>0:
                aa=B[i]
                for t in aa:
                    BB.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==0:
                        for k in range(i+1,20):
                            gg=A[k]
                            for t in gg:
                                BB.add(t)
                    if aa[j]==2:
                        for k in range(i+1,20):
                            gg=C[k]
                            for t in gg:
                                BB.add(t)
        # print(BB)
        CC=set()
        for i in range(len(C)):
            if len(C[i])>0:
                aa=C[i]
                for t in aa:
                    CC.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==0:
                        for k in range(i+1,20):
                            gg=A[k]
                            for t in gg:
                                CC.add(t)
                    if aa[j]==1:
                        for k in range(i+1,20):
                            gg=B[k]
                            for t in gg:
                                CC.add(t)
        # print(CC)
        
        AA.add(0)
        BB.add(1)
        CC.add(2)
        l1=len(AA)
        l2=len(BB)
        l3=len(CC)
        print(f'{min(l1,l2,l3)} {max(l1,l2,l3)}')

        
    if n==4:
        v=list(map(int,input().split()))
        mat=[]
        for j in range(1,23):
            t=[-1]*n
            for i in range(n):
                if j==1:
                    if v[0]==0:
                        t[0]=0
                elif j==2:
                    if i==0:
                        if v[i]!=0:
                            t[0]=(j-(i+1))/v[i]
                        else:
                            t[0]=-1
                    elif i==1:
                        if v[i]==0:
                            t[1]=0

                elif j==3:
                    if i==0:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==1:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==2:
                        if v[i]==0:
                            t[i]=0
                elif j==4:
                    if i==0:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==1:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==2:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==3:
                        if v[i]==0:
                            t[i]=0
           
                else:

                    if v[i]!=0:
                        t[i]=(j-(i+1))/v[i]
                    else:
                        t[i]=-1

            mat.append(t)
        # for i in range(22):
        #     for j in range(n)  :
        #         print(mat[i][j],end=' ')
        #     print()
        
        # if sum(t)!=0:
        # ans=list()   

        A=[-1]*(22)
        B=[-1]*(22)
        C=[-1]*(22)
        D=[-1]*(22)
        
        for b in range(n):
            # Set.add(b)
            fl =False
            SSSS=set()

            for i in range(22):
                
                # if j+1 not in Set:
                # lis1=list()
                Set=set()
                # lis2=list()
                # lis1=list(Set)
                # lis2=lis1[:]

                for j in range(0,b):
                    if mat[i][j]>0 and mat[i][b]==0:
                        Set.add(j)
                    elif mat[i][j]>mat[i][b] or mat[i][j]==0 or mat[i][j]==-1 or mat[i][b]==-1:
                        pass
                    else:
                        if fl==True:
                            if j not in SSSS:
                                Set.add(j)
                                SSSS.add(j)
                        else:
                            
                            Set.add(j)
                            # if b==n-1:
                            fl=True
                            SSSS.add(j)
                    
                
                    
                for j in range(b+1,n):
                    if mat[i][j]==0  and mat[i][b]> 0:                    
                        Set.add(j)
                    elif mat[i][j]<mat[i][b]   or mat[i][b]==0 or mat[i][j]==-1 or mat[i][b]==-1 :
                        pass
                    else:
                        if fl==True:
                            if j not in SSSS:
                                Set.add(j)
                                SSSS.add(j)
                        else:
                            Set.add(j)
                            fl=True
                            SSSS.add(j)
                lis1=list(Set)
                if b==0:
                    A[i]=lis1
                elif b==1:
                    B[i]=lis1
                elif b==2:
                    C[i]=lis1
                elif b==3:
                    D[i]=lis1
            # print(Set)
            # ans.append(len(Set))
        
        size1=A[0]
        for i in range(len(A)):
            if len(A[i])!=0:
                if A[i]!=size1:
                    size1=A[i]
                else:
                    A[i]=[]
        size2=B[0]
        for i in range(len(B)):
            if len(B[i])!=0:
                if B[i]!=size2:
                    size2=B[i]
                else:
                    B[i]=[]
        size3=C[0]
        for i in range(len(C)):
            if len(C[i])!=0: 
                if C[i]!=size3:
                    size3=C[i]
                else:
                    C[i]=[]
        size4=D[0]
        for i in range(len(D)):
            if len(D[i])!=0: 
                if D[i]!=size4:
                    size4=D[i]
                else:
                    D[i]=[]


        # print(A)
        # print(B)
        # print(C)
        # print(D)


        AA=set()
        Acopy=A[:]
        for i in range(len(Acopy)):
            if len(Acopy[i])>0:
                aa=Acopy[i]
                for t in aa:
                    AA.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==1:
                        for k in range(i+1,22):
                            gg=B[k]
                            if len(Acopy[k])==0:
                                Acopy[k]=B[k]
                            else:
                                S=set()
                                S=set(Acopy[k])
                                for y in gg:
                                    if y not in S:
                                        Acopy[k].append(y)
                            # gg=B[k]
                            for t in gg:
                                AA.add(t)
                    if aa[j]==2:
                        for k in range(i+1,22):
                            gg=C[k]
                            if len(Acopy[k])==0:
                                Acopy[k]=C[k]
                            else:
                                S=set()
                                S=set(Acopy[k])
                                for y in gg:
                                    if y not in S:
                                        Acopy[k].append(y)
                            for t in gg:
                                AA.add(t)
                    if aa[j]==3:
                        for k in range(i+1,22):
                            gg=D[k] 
                            if len(Acopy[k])==0:
                                Acopy[k]=D[k]
                            else:
                                S=set()
                                S=set(Acopy[k])
                                for y in gg:
                                    if y not in S:
                                        Acopy[k].append(y)
                            for t in gg:
                                AA.add(t)
                    
           

        # print(AA)
        BB=set()
        Bcopy=B[:]
        for i in range(len(Bcopy)):
            if len(Bcopy[i])>0:
                aa=Bcopy[i]
                for t in aa:
                    BB.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==0:
                        for k in range(i+1,22):
                            gg=A[k]
                            if len(Bcopy[k])==0:
                                Bcopy[k]=A[k]
                            else:
                                S=set()
                                S=set(Bcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Bcopy[k].append(y)
                            for t in gg:
                                BB.add(t)
                    if aa[j]==2:
                        for k in range(i+1,22):
                            gg=C[k]
                            if len(Bcopy[k])==0:
                                Bcopy[k]=C[k]
                            else:
                                S=set()
                                S=set(Bcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Bcopy[k].append(y)
                            for t in gg:
                                BB.add(t)
                    if aa[j]==3:
                        for k in range(i+1,22):
                            gg=D[k] 
                            if len(Bcopy[k])==0:
                                Bcopy[k]=D[k]
                            else:
                                S=set()
                                S=set(Bcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Bcopy[k].append(y)
                            for t in gg:
                                BB.add(t)
                 

        # print(BB)
        CC=set()
        Ccopy=C[:]
        for i in range(len(Ccopy)):
            if len(Ccopy[i])>0:
                aa=Ccopy[i]
                for t in aa:
                    CC.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==0:
                        for k in range(i+1,22):
                            gg=A[k]
                            if len(Ccopy[k])==0:
                                Ccopy[k]=A[k]
                            else:
                                S=set()
                                S=set(Ccopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ccopy[k].append(y)
                            for t in gg:
                                CC.add(t)
                    if aa[j]==1:
                        for k in range(i+1,22):
                            gg=B[k]
                            if len(Ccopy[k])==0:
                                Ccopy[k]=B[k]
                            else:
                                S=set()
                                S=set(Ccopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ccopy[k].append(y)
                            for t in gg:
                                CC.add(t)
                    if aa[j]==3:
                        for k in range(i+1,22):
                            gg=D[k]
                            if len(Ccopy[k])==0:
                                Ccopy[k]=D[k]
                            else:
                                S=set()
                                S=set(Ccopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ccopy[k].append(y) 
                            for t in gg:
                                CC.add(t)
              

        # print(CC)
        DD=set()
        Dcopy=D[:]
        for i in range(len(Dcopy)):
            if len(Dcopy[i])>0:
                aa=Dcopy[i]
                for t in aa:
                    DD.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==0:
                        for k in range(i+1,22):
                            gg=A[k]
                            if len(Dcopy[k])==0:
                                Dcopy[k]=A[k]
                            else:
                                S=set()
                                S=set(Dcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Dcopy[k].append(y)
                            for t in gg:
                                DD.add(t)
                    if aa[j]==1:
                        for k in range(i+1,22):
                            gg=B[k]
                            if len(Dcopy[k])==0:
                                Dcopy[k]=B[k]
                            else:
                                S=set()
                                S=set(Dcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Dcopy[k].append(y)
                            for t in gg:
                                DD.add(t)
                    if aa[j]==2:
                        for k in range(i+1,22):
                            gg=C[k]
                            if len(Dcopy[k])==0:
                                Dcopy[k]=C[k]
                            else:
                                S=set()
                                S=set(Dcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Dcopy[k].append(y)
                            for t in gg:
                                DD.add(t)
                 
        # print(DD)
       
        if v[1]==0:
            Bz=list()
            for i in range(len(B)):
                if len(B[i])!=0:
                    fff=B[i]
                    for tt in fff:
                        Bz.append(tt)
            if v[0]!=0:
                for pp in Bz:
                    AA.add(pp)

            

        if v[2]==0:
            Cz=list()
            for i in range(len(C)):
                if len(C[i])!=0:
                    fff=C[i]
                    for tt in fff:
                        Cz.append(tt)
            if v[1]!=0:
                for pp in Cz:
                    BB.add(pp)
            
        if v[3]==0:
            Dz=list()
            for i in range(len(D)):
                if len(D[i])!=0:
                    fff=D[i]
                    for tt in fff:
                        Dz.append(tt)
           
            if v[2]!=0:
                for pp in Dz:
                    CC.add(pp)
            


        AA.add(0)
        BB.add(1)
        CC.add(2)
        DD.add(3)
        l1=len(AA)
        l2=len(BB)
        l3=len(CC)
        l4=len(DD)
        print(f'{min(l1,l2,l3,l4)} {max(l1,l2,l3,l4)}')
        
        
        # print(AA)
        # print(BB)
        # print(CC)
        # print(DD)
    

    if n==5:

        v=list(map(int,input().split()))
        mat=[]
        for j in range(1,23):
            t=[-1]*n
            for i in range(n):
                if j==1:
                    if v[0]==0:
                        t[0]=0
                elif j==2:
                    if i==0:
                        if v[i]!=0:
                            t[0]=(j-(i+1))/v[i]
                        else:
                            t[0]=-1
                    elif i==1:
                        if v[i]==0:
                            t[1]=0

                elif j==3:
                    if i==0:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==1:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==2:
                        if v[i]==0:
                            t[i]=0
                elif j==4:
                    if i==0:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==1:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==2:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==3:
                        if v[i]==0:
                            t[i]=0
                elif j==5:
                    if i==0:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==1:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==2:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==3:
                        if v[i]!=0:
                            t[i]=(j-(i+1))/v[i]
                        else:
                            t[i]=-1
                    elif i==4:
                        if v[i]==0:
                            t[i]=0
           
                else:

                    if v[i]!=0:
                        t[i]=(j-(i+1))/v[i]
                    else:
                        t[i]=-1

            mat.append(t)
        # for i in range(22):
        #     for j in range(n)  :
        #         print(mat[i][j],end=' ')
        #     print()
        
        # if sum(t)!=0:
        # ans=list()   

        A=[-1]*(22)
        B=[-1]*(22)
        C=[-1]*(22)
        D=[-1]*(22)
        E=[-1]*(22)
        
        for b in range(n):
            # Set.add(b)
            fl=False
            SSSS=set()

            for i in range(22):
                
                # if j+1 not in Set:
                lis1=list()
                Set=set()
                # lis2=list()
                # lis1=list(Set)
                # lis2=lis1[:]

                for j in range(0,b):
                    if mat[i][j]>0 and mat[i][b]==0:
                        Set.add(j)
                    elif mat[i][j]>mat[i][b] or mat[i][j]==0 or mat[i][j]==-1 or mat[i][b]==-1:
                        pass
                    else:
                        
                        if fl==True:
                            if j not in SSSS:
                                Set.add(j)
                                SSSS.add(j)
                        else:
                            
                            Set.add(j)
                            # if b==n-1:
                            fl=True
                            SSSS.add(j)
                
                    
                for j in range(b+1,n):  
                    if mat[i][j]==0  and mat[i][b]> 0:                    
                        Set.add(j)
                    elif mat[i][j]<mat[i][b]   or mat[i][b]==0 or mat[i][j]==-1 or mat[i][b]==-1 :
                        pass
                    else:
                        if fl==True:
                            if j not in SSSS:
                                Set.add(j)
                                SSSS.add(j)
                        else:
                            
                            Set.add(j)
                            # if b==n-1:
                            fl=True
                            SSSS.add(j)
                lis1=list(Set)
                if b==0:
                    A[i]=lis1
                elif b==1:
                    B[i]=lis1
                elif b==2:
                    C[i]=lis1
                elif b==3:
                    D[i]=lis1
                elif b==4:
                    E[i]=lis1
            # print(Set)
            # ans.append(len(Set))
        
        size1=A[0]
        for i in range(len(A)):
            if len(A[i])!=0:
                if set(A[i])!=set(size1):
                    size1=A[i]
                else:
                    A[i]=[]
        size2=B[0]
        for i in range(len(B)):
            if len(B[i])!=0:
                if set(B[i])!=set(size2):
                    size2=B[i]
                else:
                    B[i]=[]
        size3=C[0]
        for i in range(len(C)):
            if len(C[i])!=0: 
                if set(C[i])!=set(size3):
                    size3=C[i]
                else:
                    C[i]=[]
        size4=D[0]
        for i in range(len(D)):
            if len(D[i])!=0: 
                if set(D[i])!=set(size4):
                    size4=D[i]
                else:
                    D[i]=[]
        size5=E[0]
      
        for i in range(len(E)):
            if len(E[i])!=0: 
                if set(E[i])!=set(size5):
                    size5=E[i]
                else:
                    E[i]=[]
        # EEE=set()
        # for i in range(len(E)):
        #     if len(E[i])!=0: 
        #         GG=E[i]
        #         for t in range(len(GG)):
        #             if GG[t] not in EEE:
        #                 EEE.add(GG[t])
        #             else:
        #                 GG.pop(GG[t])

        


        # print(A)
        # print(B)
        # print(C)
        # print(D)
        # print(E)
        

        AA=set()
        Acopy=A[:]
        for i in range(len(Acopy)):
            if len(Acopy[i])>0:
                aa=Acopy[i]
                for t in aa:
                    AA.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==1:
                        for k in range(i+1,22):
                            gg=B[k]
                            if len(Acopy[k])==0:
                                Acopy[k]=B[k]
                            else:
                                S=set()
                                S=set(Acopy[k])
                                for y in gg:
                                    if y not in S:
                                        Acopy[k].append(y)
                            # gg=B[k]
                            for t in gg:
                                AA.add(t)
                    if aa[j]==2:
                        for k in range(i+1,22):
                            gg=C[k]
                            if len(Acopy[k])==0:
                                Acopy[k]=C[k]
                            else:
                                S=set()
                                S=set(Acopy[k])
                                for y in gg:
                                    if y not in S:
                                        Acopy[k].append(y)
                            for t in gg:
                                AA.add(t)
                    if aa[j]==3:
                        for k in range(i+1,22):
                            gg=D[k] 
                            if len(Acopy[k])==0:
                                Acopy[k]=D[k]
                            else:
                                S=set()
                                S=set(Acopy[k])
                                for y in gg:
                                    if y not in S:
                                        Acopy[k].append(y)
                            for t in gg:
                                AA.add(t)
                    if aa[j]==4:
                        for k in range(i+1,22):
                            gg=E[k]
                            if len(Acopy[k])==0:
                                Acopy[k]=E[k]
                            else:
                                S=set()
                                S=set(Acopy[k])
                                for y in gg:
                                    if y not in S:
                                        Acopy[k].append(y) 
                            for t in gg:
                                AA.add(t)

        # print(AA)
        BB=set()
        Bcopy=B[:]
        for i in range(len(Bcopy)):
            if len(Bcopy[i])>0:
                aa=Bcopy[i]
                for t in aa:
                    BB.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==0:
                        for k in range(i+1,22):
                            gg=A[k]
                            if len(Bcopy[k])==0:
                                Bcopy[k]=A[k]
                            else:
                                S=set()
                                S=set(Bcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Bcopy[k].append(y)
                            for t in gg:
                                BB.add(t)
                    if aa[j]==2:
                        for k in range(i+1,22):
                            gg=C[k]
                            if len(Bcopy[k])==0:
                                Bcopy[k]=C[k]
                            else:
                                S=set()
                                S=set(Bcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Bcopy[k].append(y)
                            for t in gg:
                                BB.add(t)
                    if aa[j]==3:
                        for k in range(i+1,22):
                            gg=D[k] 
                            if len(Bcopy[k])==0:
                                Bcopy[k]=D[k]
                            else:
                                S=set()
                                S=set(Bcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Bcopy[k].append(y)
                            for t in gg:
                                BB.add(t)
                    if aa[j]==4:
                        for k in range(i+1,22):
                            gg=E[k] 
                            if len(Bcopy[k])==0:
                                Bcopy[k]=E[k]
                            else:
                                S=set()
                                S=set(Bcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Bcopy[k].append(y)
                            for t in gg:
                                BB.add(t)

        # print(BB)
        CC=set()
        Ccopy=C[:]
        for i in range(len(Ccopy)):
            if len(Ccopy[i])>0:
                aa=Ccopy[i]
                for t in aa:
                    CC.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==0:
                        for k in range(i+1,22):
                            gg=A[k]
                            if len(Ccopy[k])==0:
                                Ccopy[k]=A[k]
                            else:
                                S=set()
                                S=set(Ccopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ccopy[k].append(y)
                            for t in gg:
                                CC.add(t)
                    if aa[j]==1:
                        for k in range(i+1,22):
                            gg=B[k]
                            if len(Ccopy[k])==0:
                                Ccopy[k]=B[k]
                            else:
                                S=set()
                                S=set(Ccopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ccopy[k].append(y)
                            for t in gg:
                                CC.add(t)
                    if aa[j]==3:
                        for k in range(i+1,22):
                            gg=D[k]
                            if len(Ccopy[k])==0:
                                Ccopy[k]=D[k]
                            else:
                                S=set()
                                S=set(Ccopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ccopy[k].append(y) 
                            for t in gg:
                                CC.add(t)
                    if aa[j]==4:
                        for k in range(i+1,22):
                            gg=E[k] 
                            if len(Ccopy[k])==0:
                                Ccopy[k]=E[k]
                            else:
                                S=set()
                                S=set(Ccopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ccopy[k].append(y)
                            for t in gg:
                                CC.add(t)

        # print(CC)
        DD=set()
        Dcopy=D[:]
        for i in range(len(Dcopy)):
            if len(Dcopy[i])>0:
                aa=Dcopy[i]
                for t in aa:
                    DD.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==0:
                        for k in range(i+1,22):
                            gg=A[k]
                            if len(Dcopy[k])==0:
                                Dcopy[k]=A[k]
                            else:
                                S=set()
                                S=set(Dcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Dcopy[k].append(y)
                            for t in gg:
                                DD.add(t)
                    if aa[j]==1:
                        for k in range(i+1,22):
                            gg=B[k]
                            if len(Dcopy[k])==0:
                                Dcopy[k]=B[k]
                            else:
                                S=set()
                                S=set(Dcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Dcopy[k].append(y)
                            for t in gg:
                                DD.add(t)
                    if aa[j]==2:
                        for k in range(i+1,22):
                            gg=C[k]
                            if len(Dcopy[k])==0:
                                Dcopy[k]=C[k]
                            else:
                                S=set()
                                S=set(Dcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Dcopy[k].append(y)
                            for t in gg:
                                DD.add(t)
                    if aa[j]==4:
                        for k in range(i+1,22):
                            gg=E[k]
                            if len(Dcopy[k])==0:
                                Dcopy[k]=E[k]
                            else:
                                S=set()
                                S=set(Dcopy[k])
                                for y in gg:
                                    if y not in S:
                                        Dcopy[k].append(y) 
                            for t in gg:
                                DD.add(t)

        # print(DD)
        EE=set()
        Ecopy=E[:]
        for i in range(len(Ecopy)):
            if len(Ecopy[i])>0:
                aa=Ecopy[i]
                for t in aa:
                    EE.add(t)
                for j in range(len(aa)):
                    
                    if aa[j]==0:
                        for k in range(i+1,22):
                            gg=A[k]
                            if len(Ecopy[k])==0:
                                Ecopy[k]=A[k]
                            else:
                                S=set()
                                S=set(Ecopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ecopy[k].append(y)
                            for t in gg:
                                EE.add(t)
                    if aa[j]==1:
                        for k in range(i+1,22):
                            gg=B[k]
                            if len(Ecopy[k])==0:
                                Ecopy[k]=B[k]
                            else:
                                S=set()
                                S=set(Ecopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ecopy[k].append(y)
                            for t in gg:
                                EE.add(t)
                    if aa[j]==2:
                        for k in range(i+1,22):
                            gg=C[k]
                            if len(Ecopy[k])==0:
                                Ecopy[k]=C[k]
                            else:
                                S=set()
                                S=set(Ecopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ecopy[k].append(y)
                            for t in gg:
                                EE.add(t)
                    if aa[j]==3:
                        for k in range(i+1,22):
                            gg=D[k]
                            if len(Ecopy[k])==0:
                                Ecopy[k]=D[k]
                            else:
                                S=set()
                                S=set(Ecopy[k])
                                for y in gg:
                                    if y not in S:
                                        Ecopy[k].append(y) 
                            for t in gg:
                                EE.add(t)
        # print(EE)
        

        if v[1]==0:
            Bz=list()
            for i in range(len(B)):
                if len(B[i])!=0:
                    fff=B[i]
                    for tt in fff:
                        Bz.append(tt)
            if v[0]!=0:
                for pp in Bz:
                    AA.add(pp)

            

        if v[2]==0:
            Cz=list()
            for i in range(len(C)):
                if len(C[i])!=0:
                    fff=C[i]
                    for tt in fff:
                        Cz.append(tt)
            
            if v[1]!=0:
                for pp in Cz:
                    BB.add(pp)
            
        if v[3]==0:
            Dz=list()
            for i in range(len(D)):
                if len(D[i])!=0:
                    fff=D[i]
                    for tt in fff:
                        Dz.append(tt)
           
            if v[2]!=0:
                for pp in Dz:
                    CC.add(pp)
        if v[4]==0:
            Ez=list()
            for i in range(len(E)):
                if len(E[i])!=0:
                    fff=E[i]
                    for tt in fff:
                        Ez.append(tt)
       
            if v[3]!=0:
                for pp in Ez:
                    DD.add(pp)
        
        AA.add(0)
        BB.add(1)
        CC.add(2)
        DD.add(3)
        EE.add(4)
        l1=len(AA)
        l2=len(BB)
        l3=len(CC)
        l4=len(DD)
        l5=len(EE)
        print(f'{min(l1,l2,l3,l4,l5)} {max(l1,l2,l3,l4,l5)}')
      
      
      
        print(AA)
        print(BB)
        print(CC)
        print(DD)
        print(EE)
    
        # print(A)
        # print(B)
        # print(C)
        # print(D)
        # print(E)


  
        
            













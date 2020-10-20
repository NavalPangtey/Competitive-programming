try :
    for i in range(int(input())):
        n = int(input())
        N=(4*n)-1
        X=[]
        Y=[]
        s=[]
        for i in range(N):
            s=list(map(int, input().split()))
            X.append(s[0])
            Y.append(s[1])
            s=[]

        X.sort()
        Y.sort()
        # print(X)
        # print(Y)
        x=0
        y=0
        i=0
        while i<N:
            if i==N-1:
                x=X[i]
                break
            elif X[i]==X[i+1]:
                i=i+2
            else:
                x=X[i]
                break
        i=0
        while i < N:
            if i==N-1:
                y=Y[i]
                break
            elif Y[i] == Y[i + 1]:
                i=i+2
            else:
                y = Y[i]
                break

        # for i in range(N):
        #     if Y[i]== Y[i+1]:
        #         i=i+2
        #     else:
        #         y=Y[i]
        #         break
       # for i in range(N):
        #     if X[i]==X[i+1] or  X[i]==X[i-1]:



        # for i in range(4*n):
        #     if X[i]==X[i+1] and Y[i]!=Y[i+1]:
        #         pass
        #     elif X[i]!=X[i+1] and Y[i]==Y[i+1]:
        #         pass
        #     elif i==N-1:
        #         X[i]=X[i-1]
        #         Y[i]=Y[i-1]+1
        print('{} {}'.format(x,y))
        # print(X)
        # print(Y)
except Exception:
    pass

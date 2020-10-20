try:
    for _ in range(int(input())):
        C,R= map(int,input().split())
        countC=0
        countR=0
        RC=C
        RR=R
        UU=0
        if C<10 and R<10:
            print(f'1 1')
            continue
        
        elif C<10 and R>=10:
            print(f'0 1')
            continue

        
        elif R<10 and C>=10:
            print(f'1 1')
            continue
        
        if C<R:
            while C:
                if C>=900000:
                    C=C-900000
                    countC+=100000
                elif C>=90000:
                    C=C-90000
                    countC+=10000
                elif C>=9000:
                    C=C-9000
                    countC+=1000
                elif C>=900:
                    C=C-900
                    countC+=100
                elif C>=90:
                    C=C-90
                    countC+=10               
                elif C<90:
                    C=C-9
                    countC+=1
        
                if C==0:
                    break
                if C<9:
                    UU=C
                    C=C-C
                    countC+=1
            if RR<=(RC-UU)+9:
                print(f'1 {countC}')
            else:
                print(f'0 {countC}')

                
        else:
            while R:
                if R>=900000:
                    R=R-900000
                    countR+=100000
                elif R>=90000:
                    R=R-90000
                    countR+=10000
                elif R>=9000:
                    R=R-9000
                    countR+=1000
                elif R>=900:
                    R=R-900
                    countR+=100
                elif R>=90:
                    R=R-90
                    countR+=10               
                elif R<90:
                    R=R-9
                    countR+=1
                    
                if R==0:
                    break
                if R<9:
                    R=R-R
                    countR+=1
            print(f'1 {countR}')

        # if countC<countR:
        #     print(f'0 {countC}')
        # else:
        #     print(f'1 {countR}')

except Exception :
    pass

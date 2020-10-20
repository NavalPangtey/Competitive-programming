for _ in range(int(input())):
    C,R= map(int,input().split())
    countC=0
    countR=0
    check={5,6,7,8,9}

    if C<10 and R<10:
        print('1 1')
        continue
    

    if C<10 and R>=10:
        print('0 1')
        continue

       
    if R<10 and C>=10:
        print('1 1')
        continue

    # if C//2 in check and R//2 in check:
    #     print('1 2')
    #     continue
    
    
    # if C//2 in check and R//2 not in check:
    #     print('0 2')
    #     continue


    # if C//2 not in check and R//2 in check:
    #     print('1 2')
    #     continue

    if C<R:
        if R<=2*C:
            i=9
            while i>=5 :
                if C%i==0:
                    C=C-(i*2)
                    countC+=2
                    i=9
                    if C==0:
                        break
                    elif C<10:
                        countC+=1
                        break
                else:
                    i=i-1

            i=9
            while i>=5:
                if R%i==0:
                    R=R-(i*2)
                    countR+=2
                    i=9
                    if R==0:
                        break
                    if R<10:
                        countR+=1
                        break
                else:
                    i=i-1
        

            if countC<countR:
                print(f"{0} {countC}")
            else:
                print(f'{1} {countR}')
            
        else:
            i=9
            while i>=5 :
                if C%i==0:
                    C=C-(i*2)
                    countC+=2
                    i=9
                    if C==0:
                        break
                    elif C<10:
                        countC+=1
                        break
                else:
                    i=i-1
            print(f"{0} {countC}")
            

    elif C>=R:
        if C<=2*R:
            i=9
            while i>=5 :
                if C%i==0:
                    C=C-(i*2)
                    countC+=2
                    i=9
                    if C==0:
                        break
                    elif C<10:
                        countC+=1
                        break
                else:
                    i=i-1

            i=9
            while i>=5:
                if R%i==0:
                    R=R-(i*2)
                    countR+=2
                    i=9
                    if R==0:
                        break
                    if R<10:
                        countR+=1
                        break
                else:
                    i=i-1

            
            if countC<countR:
                print(f"{0} {countC}")
            else:
                print(f'{1} {countR}')

        else:

            i=9
            while i>=5:
                if R%i==0:
                    R=R-(i*2)
                    countR+=2
                    i=9
                    if R==0:
                        break
                    if R<10:
                        countR+=1
                        break
                else:
                    i=i-1
            
            print(f'{1} {countR}')
            







for _ in range(int(input())):
    n=int(input())
    if n%7==0:
        print(f'83')
            
    else:
        nn=n
        tt=0
        for i in range(8):
            nn+=1
            tt+=1
            if nn%7==0:
                break

        # print(nn)
        # print(tt)

   
        if tt==6:
            print(f'83')
        elif tt==5:
            print(f'83 83')
        elif tt==4:
            print(f'83 83 69')
        elif tt==3:
            print(f'83 83 69 67')
        elif tt==2:
            print(f'83 83 69')
        elif tt==1:
            print(f'83 83')

       
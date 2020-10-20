
try :
    for i in range(int(input())):


        n= int(input())



        if n%2==0:
            a=n//2
            print('{} {}'.format(a,a))
        else:
            if n%3==0:
                a=n//3
                b=n-a
                print('{} {}'.format(a,b))
            else:
                a=n-1;
                b=1
                print('{} {}'.format(a,b))


        # a=[]
        # for i in range(n):
        #     a.append(2)

        # for i in range(n):
        #     print(a[i],end=" ")
        # print()


except Exception:
    pass

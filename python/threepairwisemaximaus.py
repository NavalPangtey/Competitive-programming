for _ in range(int(input())):
    k= list(map(int,input().split()))
    x=k[0]
    y=k[1]
    z=k[2]
    # a,b,c=1,1,1
    # if x==y and y==z:
    #     print('YES')
    #     print('{} {} {}'.format(x,y,z))
    # else:
    #     if x==y:
    #         a=x
    #     elif x!=y:
    #         b=x
    #     if x==z:
    #         b=z
    #     else:
    #         if b>=z:
    #
    if x==y or x==z or y==z :
        if x==y:
            if z> x:
                print('NO')
            else:
                print('{} {} {}'.format(x, z, 1))
        elif x==z:
            if y > x:
                print('NO')
            else:
                print('{} {} {}'.format(x, y, 1))
        elif y == z:
            if x > y:
                print('NO')
            else:
                print('{} {} {}'.format(x, y, 1))
    else:
        print('NO')





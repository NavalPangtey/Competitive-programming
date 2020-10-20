for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    # s.sort()
    one=0
    zero=0
    for i in s:
        if i==1:
            one+=1
        else:
            zero+=1
    # print(one)
    # print(zero)
    h=n//2
    if n==2:
        if one==2:
            print(2)
            print('1 1')
        else:
            print(1)
            print("0")
    elif h%2==0:
        print(n-(n//2))
        if one>=n//2 :
            for i in range(n//2):
                print('1',end=" ")
            print()
        elif zero>=n//2:
            for i in range(n//2):
                print('0',end=" ")
            print()
    else:
        if one>=(n//2)+1 :
            print((n//2)+1)
            for i in range(n//2+1):
                print('1',end=" ")
            print()
        elif zero>=n//2:
            print(n-(n//2))
            for i in range((n//2)):
                print('0',end=" ")
            print()

    
    # if s[n-1]==0:
    #     print(n//2)
    #     for i in range(n//2):
    #         print('0',end=" ")
    #     print()
    
    # elif s[0]==1:
    #     print(n//2)
    #     for i in range(n//2):
    #         print('1',end=" ")
    #     print()
    
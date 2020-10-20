def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    print(('{} ' * len(unique_list)).format(*unique_list))

for _ in range(int(input())):
    n= int(input())

    a=list(map(int,input().split()))
    unique(a)
    # while i<2*n:
    #     if a[i]
    #     b.append(a[i])
    #     i=i+2
    # print(('{} ' * len(b)).format(*b))



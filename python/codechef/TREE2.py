for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    Set=set(a)
    l=list(Set)
    for num in l:
        if num==0:
            l.remove(0)

    print(len(l))
    
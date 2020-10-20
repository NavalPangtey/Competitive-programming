
from functools import reduce
from more_itertools import powerset

def check_duplicates(my_list):
    seen = {}
    for item in my_list:
        if seen.get(item):
            return True
        seen[item] = True
    return False

for _ in range(int(input())):
    n= int(input())
    a= list(map(int,input().split()))
    check= set()
    flag=False
    sublist = []
    for i in range(len(a) + 1):
        for j in range(i + 1, len(a) + 1):
            sub = a[i:j]
            sublist.append(sub)


    # sublist=list(powerset(a))
    # sublist.pop(0)
    # print(sublist)
    for i in range(len(sublist)):
        check.add(reduce(lambda x, y: x | y, sublist[i]))

    flag=check_duplicates(check)


    if flag==True:
        print('NO')
    else:
        print('YES')

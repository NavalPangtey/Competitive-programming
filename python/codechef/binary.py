import math
from collections import defaultdict


def binconcat(a, b):
    abin = bin(a).replace("0b", "")
    bbin = bin(b).replace("0b", "")
    apb = str(abin) + str(bbin)
    bpa = str(bbin) + str(abin)
    n1 = int(apb,2)
    n2 = int(bpa, 2)
    return n1-n2


t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    binc = []
    if n<=500:
        for i in range(n):
            for j in range(n):
                binc.append(binconcat(a[i],a[j]))
        print(max(binc))
    else:
        ans = 0
        tmp = max(a)
        for x in range(n):
            binc.append(binconcat(tmp,a[x]))
        print(max(binc))

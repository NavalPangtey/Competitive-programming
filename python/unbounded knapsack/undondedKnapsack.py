#Rod cutting problem
def unbondedKnapSack(price,length,size,N):
    t = [[0 for x in range(size+ 1)] for x in range(N + 1)]
    for i in range(N + 1):
        for j in range(size + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif (length[i - 1] <= j):
                t[i][j] = max(price[i - 1] + t[i ][j - length[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]

    return t[N][size]


length=[1,2,3,4,5,6,7,8 ]
price=[1,5,8,9,10,17,17,20]
N=8
size=len(length)

print(unbondedKnapSack(price,length,size,N))
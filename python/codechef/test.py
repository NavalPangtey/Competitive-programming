num = []
test = int(input())
for _ in range(test):
    n, k = input().split()
    n = int(n)
    k = int(k)
    ls = []
    count = 0
    ls = input().split()
    for _ in range(k):
        if ls[n - 1] == 'T':
            ls.pop()
        elif ls[n - 1] == 'H':
            for i in range(n):
                if ls[i] == 'T':
                    ls[i] = 'H'
                else:
                    ls[i] = 'T'
        n -= 1
    for i in range(n):
        if ls[i] == 'H':
            count += 1
    num.append(count)
for i in range(test):
    print(num[i])
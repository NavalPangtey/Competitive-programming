for _ in range(int(input())):
    n, m = map(int, input().split())
    output = list()
    l = list(map(int, input().split()))

    for num in l:
        if num % m == 0:
            output.append(1)
        else:
            output.append(0)

    print("".join(str(x) for x in output))










def frequncycheck(s):
    frequancy = [0] * 26
    n = len(s)
    for i in range(n):
        frequancy[ord(s[i]) - 97] += 1
    for i in range(26):
        if (frequancy[i] % 2 == 1):
            return False
    return True

for _ in range(int(input())):
    n= int(input())
    s= str(input())
    if n%2!=0:
        print('NO')
    else:
        if frequncycheck(s):
            print('YES')
        else:
            print('NO')



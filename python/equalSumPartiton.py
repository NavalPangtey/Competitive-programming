def eqaulsum(arr,n):
    sum=0
    for i in range(n):
        sum+=arr[i]
    if sum%2!=0:
        return False
    elif sum%2==0:
        return subsetsum(arr,sum//2,n)

def subsetsum(arr,sum,n):
    t = ([[0 for j in range(sum + 1)] for i in range(n + 1)])
    for i in range(n + 1):
        t[i][0] = True
    for i in range(1, sum + 1):
        t[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j >= arr[i - 1]:
                t[i][j] = (t[i - 1][j - arr[i - 1]] or t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    return t[n][sum]
arr=[2,20,6,8,1,3]
n=6
print(eqaulsum(arr,n))
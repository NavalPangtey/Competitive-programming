
# nums =[12,345,2,6,7896]
# n = len(nums)
# c = 0
# m = 0
# for i in nums:
#     t = list(map(int, str(i)))
#     c = len(t)
#     if c > m and c % 2 == 0:
#         m = c
#
# print(m)
A=[-4,-1,0,3,10]

for i in range(len(A)):
    A[i] = A[i] * A[i]
A.sort()
print(A)
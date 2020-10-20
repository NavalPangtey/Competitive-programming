class Solution:

    def __init__(self,nums,S):
        self.nums=nums
        self.S=S

    def findTargetSumWays(self):
        if len(nums) > 20 or S > 1000:
            return 0
        total, n = 0, len(nums)
        total=sum(nums)
        # for i in nums:
        #     total += i
        if (total+S)%2 != 0:
            return 0
        else:
            summ = (total+S)//2
        t = [[0 for i in range(summ+1)] for i in range(n+1)]
        t[0][0] = 1
        for i in range(1, n+1):
            if nums[i-1] == 0:
                t[i][0] = 2*t[i-1][0]
            else:
                t[i][0] = t[i-1][0]
            # t[i][0]=1
        for i in range(1, summ+1):  
            t[0][i] = 0
        self.countSubsetSum(nums, summ, n, t)
        return t[n][summ]

    def countSubsetSum(self, nums, summ, n, t):
        for i in range(1, n+1):
            for j in range(1, summ+1):
                if nums[i-1] <= j:
                    t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t

nums=[0,1,1,2,3]
S=1
ala=Solution(nums,S)
print(Solution.findTargetSumWays(ala))
class Solution:
    def climbStairs(self, n: int) -> int:
        ans=[0]*n
        for i in range(n):
            if(i == 0): ans[i] = 1
            elif(i==1): ans[i] = 2
            else: ans[i] = ans[i-1]+ans[i-2]
        return ans[n-1]
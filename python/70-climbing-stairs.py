class Solution:
	#动态规划
    def climbStairs(self, n: int) -> int:
        ans=[0]*n
        for i in range(n):
            if(i == 0): ans[i] = 1
            elif(i==1): ans[i] = 2
            else: ans[i] = ans[i-1]+ans[i-2]
        return ans[n-1]
    #直接用数学的思想当前阶梯等于前面两个阶梯方法之和
    def climbStairs(self, n: int) -> int:
        if(n == 1): return 1
        if(n == 2): return 2
        low = 1
        height = 2
        rst = 0
        for i in range(3, n):
            rst = low + height
            low = height
            height = rst
        return rst

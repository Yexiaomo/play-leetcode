class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
            动态规划问题
            从下往上开始计算, 当前方框的值等于左边加上上一个
        '''
        if(m==1 or n==1): return 1
        ans = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                #网格的第一个元素值为1
                if(i==0 and j==0): ans[0][0] = 1
                #网格的左边界,上边界值都为1
                elif(i==0 or j==0): ans[i][j] =1
                #网格内部的方格值为左边值+上边值
                else: ans[i][j] = ans[i-1][j]+ans[i][j-1]
        return ans[m-1][n-1]
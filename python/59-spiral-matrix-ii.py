class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if(n<=0): return
        l, r, t, b = 0, n - 1, 0, n - 1
        rst = [[-1 for i in range(n)] for i in range(n)]
        num, N = 1, n * n
        while(num<=N):
            #顶部,从左到右
            for i in range(l, r+1):
                rst[t][i] = num
                num+=1
            #右侧,从上往下
            t+=1
            for i in range(t, b+1):
                rst[i][r] = num
                num+=1
            #底部,从右往左
            r-=1
            for i in range(r, l-1, -1):
                rst[b][i] = num
                num+=1
            #左侧,从下往上
            b-=1
            for i in range(b, t-1, -1):
                rst[i][l] = num
                num+=1
            l+=1
        return rst
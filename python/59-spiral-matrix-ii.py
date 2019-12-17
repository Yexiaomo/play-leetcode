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

    # 腾讯计划, 2019/12/17, 方法不是很好
    def generateMatrix(self, n: int):
        if(n<=0): return []
        if(n==1): return [[1]]
        circls = (n-1)//2 + 1
        nums = 1
        output = [[0 for i in range(n)] for i in range(n)]
        ml = nl = 0
        mr = nr = n-1
        for i in range(circls): 
            mi = ni = i
            # 顶部, 从左到右
            while(ni < nr):
                output[mi][ni] = nums
                nums+=1
                ni+=1
            # 右侧, 从上到下到右
            while(mi < mr):
                output[mi][ni] = nums
                nums+=1
                mi+=1
            # 底部.从右到左
            while(ni > nl):
                output[mi][ni] = nums
                nums+=1
                ni-=1
            # 左侧,从下到上
            while(mi > ml):
                output[mi][ni] = nums
                nums+=1
                mi-=1
            # 更新边界值
            ml = nl = ml+1
            mr = nr = mr-1
        # 处理特殊情况
        if(n %2 != 0): output[mi][ni] = nums
        return output

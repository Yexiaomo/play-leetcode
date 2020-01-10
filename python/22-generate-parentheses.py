class Solution:
    #分析一下,肯定有一对括号包含所有
    #解题参考链接
    #https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''
        def dfs(cur_str, left, right):
            """
            :param cur_str:从根节点到叶子节点的路径字符串
            :param left: 左括号还可以使用的次数
            :param right: 右括号还可以使用的次数
            :return:
            """
            if(left == 0 and right == 0):
                res.append(cur_str)
                return
            if(right < left): return
            if(left > 0): dfs(cur_str + '(', left-1, right)
            if(right > 0): dfs(cur_str + ')', left, right-1)
        dfs(cur_str, n, n)
        return res

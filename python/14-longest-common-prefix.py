class Solution:
    # 腾讯计划2019/12/05
    # 前向扫描
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strslen = len(strs)
        if(strslen <= 0): return ""
        ans = strs[0]
        for i in range(1, strslen):
            while(strs[i].find(ans) != 0):
                ans = ans[:-1]
                if(ans == ''): return ''
        return ans    
    
    # 评论区学到的,利用ASCII码
    # 只需要找到最长字符串,最短字符串两者进行比较
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
    
    # 评论区学到的,利用zip函数
    # 将数组中所有的字符串进行元组化
    # 元组化后,再对每个元组进行set, 就可以看成一个字符串的一个字符
    # 如果set后,长度为 1, 那么就说明这个数组中每个字符串当前位置的字符都相等
    def longestCommonPrefix(self, strs):
        prefix = []
        for t in zip(*strs):
            s = set(t)
            if(len(s) == 1):
                prefix.append(s.pop())
            else:
                break
        return "".join(prefix)

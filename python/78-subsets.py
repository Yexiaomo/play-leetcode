class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rst = [[]]
        if(not nums): return rst
        def fun(node, ans):
            for i in range(len(ans)):
                tmp = sorted(node + [ans[i]])
                if(not (tmp in rst)):
                    rst.append(tmp)
                    fun(tmp, ans[:i]+ans[i+1:])
                else:
                    continue
        fun([], nums)
        return rst
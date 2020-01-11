class Solution:
	
    #参考大神的思路:直接从前遍历，遇到一个数就把所有子集加上该数组成新的子集
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            for subres in res.copy():
                res.append(subres+[i])
        return res

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
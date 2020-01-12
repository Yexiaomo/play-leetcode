class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rst = []
        def helpPermute(subRst, subNums):
            if(not subNums): rst.append(subRst)
            for i in range(len(subNums)):
                helpPermute(subRst+[subNums[i]], subNums[:i]+subNums[i+1:])
        helpPermute([], nums)
        return rst
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rst = []
        def digui(s, cutNums):
            if(not cutNums):
                rst.append(s)
            for i in range(len(cutNums)):
                digui(s+[cutNums[i]], cutNums[:i]+cutNums[i+1:])
        digui([], nums)
        return rst
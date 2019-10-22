class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(not nums):
            return
        rst = nums[0]
        sum = 0
        for n in nums:
            sum = (sum+n) if(sum > 0) else n
            rst = max(sum,rst)
        return rst
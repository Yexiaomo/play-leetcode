class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rst_len = 1 if(nums) else 0
        for i in range(1, len(nums)):
            if(nums[i] > nums[rst_len-1]):
                nums[rst_len] = nums[i]
                rst_len += 1
        return rst_len
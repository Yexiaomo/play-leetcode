class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rstLen = 1 if(nums) else 0
        for i in range(1, len(nums)):
            if(nums[i] > nums[rstLen-1]):
                nums[rstLen] = nums[i]
                rstLen += 1
        return rstLen
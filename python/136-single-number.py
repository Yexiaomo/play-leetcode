class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        flag = 0
        for n in nums:
            flag ^= n
        return flag
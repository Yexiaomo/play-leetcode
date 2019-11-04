class Solution:
    #第一种 利用位运算,异或运算符
    def singleNumber(self, nums: List[int]) -> int:
        flag = 0
        for n in nums:
            flag ^= n
        return flag
    #第二种 利用数学的思想: 2*(a+b)-(a+b+a) = b
    def singleNumber(self, nums: List[int]) -> int:
        return 2*(sum(set(nums))) - sum(nums)
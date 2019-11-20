class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #定义两个数组, 分别保存当前位置元素的左边乘积,和右边乘积
        #后面两个for循环可以写成一个
        lenNums = len(nums)
        nLeft = [1]*lenNums
        nRight = nLeft.copy()
        for i in range(1, lenNums):
            nLeft[i] = nLeft[i-1]*nums[i-1]
        for i in range(lenNums-2, -1,-1):
            nRight[i] = nRight[i+1]*nums[i+1]
        for i in range(lenNums):
            nLeft[i] *= nRight[i]
        return nLeft

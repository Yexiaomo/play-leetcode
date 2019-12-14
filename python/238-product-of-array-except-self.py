class Solution:
    # 改良版: 最后的输出数组使用map函数
    '''思路: 定义两个数组
        leftNumsProduct保存当前位置元素左边的乘积
        rightNumsProduct保存当前位置元素右边的乘积
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        leftNumsProduct = [1]*len_nums
        for i in range(1, len_nums):
            leftNumsProduct[i] = leftNumsProduct[i-1]* nums[i-1]
        rightNumsProduct = [1]*len_nums
        for i in range(len_nums-2, -1, -1):
            rightNumsProduct[i] = rightNumsProduct[i+1]* nums[i+1]
        return map(lambda a,b: a*b, leftNumsProduct, rightNumsProduct)

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

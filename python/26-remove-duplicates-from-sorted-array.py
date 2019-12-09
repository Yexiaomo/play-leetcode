class Solution:
    '''
    思路:很明显,双指针,一慢一快
    ①快指针指向的元素判断是否与慢指针指向的元素是否一样
    ② 若相同,则快+1, 慢不动
    ③ 若不同,则慢+1, 将快指向的元素赋值给慢指向的位置
    ④循环以上,直至结束
'''
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if(len_nums <= 1): return len_nums
        slow, fast = 0, 1
        while(fast < len_nums):
            if(nums[fast] != nums[slow]):
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+1
    def removeDuplicates(self, nums: List[int]) -> int:
        rst_len = 1 if(nums) else 0
        for i in range(1, len(nums)):
            if(nums[i] > nums[rst_len-1]):
                nums[rst_len] = nums[i]
                rst_len += 1
        return rst_len

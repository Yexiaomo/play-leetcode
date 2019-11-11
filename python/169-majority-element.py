class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if(not nums): return None
        subLen = len(nums)//2
        ans = {}
        max = float("-inf")
        rst = nums[0]
        for i in nums:
            if(i in ans):
                ans[i] += 1
                if(ans[i] > max):
                    max = ans[i]
                    rst = i
                    if(max > subLen): return rst
            else:
                ans[i] = 1
        return rst
    # 后来发现一种有一个条件是-->众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素 ~_~
    def majorityElement(self, nums: List[int]) -> int:
    for i in nums[len(nums)//2:]:
        if nums.count(i) > len(nums)//2:
            return i
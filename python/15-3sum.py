class Solution:
    # 思路
    # 先排序,然后以第一个为基准
    # 如果当前i值大于0,那么结束循环
    #   如果不大于0,那么使用双指针,查询是否有两个元素使得当前三个元素相加为0
    #   找到当前三个元素等于0的情况下,追加到结果中
    #     如果此时l<r,双指针再一起移动,再对三个值进行判断
    #   如果3sum大于0,右指针移动
    #   如果3sum小于0,左指针移动
    #  循环以上,直至return
    
    #改良版
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        if(len_nums < 3): return None
        nums.sort()
        rst = []
        for i in range(0, len_nums-2):
            if(nums[i] > 0): break
            if(i == 0 or nums[i] > nums[i-1]):
                l = i+1
                r = len_nums-1
                while(l<r):
                    tmpSum = nums[i] + nums[l] + nums[r]
                    if(tmpSum == 0):
                        rst.append([nums[i], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while(l < r and nums[l] == nums[l-1]):
                            l+=1
                        while(l < r and nums[r] == nums[r+1]):
                            r-=1
                    elif(tmpSum>0):
                        r-=1
                    else:
                        l+=1
        return rst
    # 初始版
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rst = []
        numsLen = len(nums)
        for i in range(numsLen):
            if((i == 0) or nums[i] > nums[i-1]):
                l = i+1
                r = numsLen - 1
                while(l < r):
                    tmp_sum = nums[i] + nums[l] + nums[r]
                    if(tmp_sum == 0):
                        rst.append([nums[i], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while(l < r and nums[l] == nums[l-1]):
                            l+=1
                        while(r>l and nums[r] == nums[r+1]):
                            r-=1
                    elif(tmp_sum > 0):
                        r-=1
                    else:
                        l+=1
        return rst

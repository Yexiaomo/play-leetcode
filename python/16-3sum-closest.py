class Solution:
    # 改良版
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        if(len_nums < 3): return None
        nums.sort()
        rst = nums[0] + nums[1] + nums[2]
        for i in range(len_nums):
            if(i == 0 or nums[i] != nums[i-1]):
                l = i+1
                r = len_nums-1
                while(l < r):
                    tmp = nums[i] + nums[l] + nums[r]
                    if(tmp == target): return tmp
                    if(abs(tmp-target) < abs(rst-target)):
                        rst = tmp
                    if(tmp > target):
                        r-=1
                        # 防止重复判断
                        while(l<r and nums[r] == nums[r+1]):
                            r-=1
                    else:
                        l+=1
                        # 防止重复判断
                        while(l<r and nums[l] == nums[l-1]):
                            l+=1
        return rst
    # 原版
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        len_nums = len(nums)
        min = nums[0] + nums[1]+nums[2]
        for i in range(len_nums):
            if(i < 0 and nums[i] == nums[i-1]):
                continue
            l = i+1
            r = len_nums - 1
            while(l < r):
                tmp = nums[i] + nums[l] + nums[r]
                if(tmp == target):
                    return tmp
                if(abs(tmp-target) < abs(min-target)):
                    min = tmp
                if(tmp > target):
                    r-=1
                else:
                    l+=1
        return min
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         len_nums = len(nums)
#         min = nums[0] + nums[1]+nums[2]
#         for i in range(len_nums):
#             if(i == 0 or nums[i]>nums[i-1]):
#                 l = i+1
#                 r = len_nums - 1
#                 while(l < r):
#                     '''
#                         原来的判断条件:
#                         abs(tmp -target) > abs(min-target)
#                         结果却是: 113 / 125 个通过测试用例
#                         case:
#                             [1,2,4,8,16,32,64,128]
#                             82
#                         不通过
#                         感觉需要更换判断条件, 这个不太行
#                     '''
#                     tmp = nums[i] + nums[l] + nums[r]
#                     old = min-target
#                     new = tmp-target
#                     print(nums[i],nums[l],nums[r],tmp)
#                     if(new == 0):
#                         return tmp
#                     if(abs(new) > abs(old)):
#                         if(new > 0):
#                             r-= 1
#                         else:
#                             l+=1
#                     elif(abs(tmp-target) < abs(min-target)):
#                         min = tmp
#                         if(new < 0):
#                             l+=1
#                         else:
#                             r-=1
#                     else:
#                         l+=1
#                         r-=1
#                         while(l < r and nums[l] == nums[l-1]):
#                             l+=1
#                         while(r>l and nums[r] == nums[r+1]):
#                             r-=1
#         return min

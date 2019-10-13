class Solution:
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
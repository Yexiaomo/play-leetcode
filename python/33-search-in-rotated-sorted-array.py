class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        if(len_nums == 0): return -1
        i = 0 if(target >= nums[0]) else (len_nums-1)
        while(target > nums[i] and i < (len_nums-1)):
            if(i>0 and nums[i] <= nums[i-1]):
                break
            else:
                i+=1
        while(target < nums[i] and i > 0):
            if(i<(len_nums-1) and nums[i] >= nums[i+1]):
                break
            else:
                i-=1
        return i if(target == nums[i]) else -1
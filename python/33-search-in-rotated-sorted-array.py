class Solution:
    #折半查找
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        if(len_nums < 1): return -1
        
        left, right = 0, len_nums-1
        mid = left + (right - left)//2
        while(left<=right):
            if(target == nums[mid]):
                return mid
            if(nums[left] <= nums[mid]):
                if(target >= nums[left] and target <= nums[mid]):
                    right = mid-1
                else:
                    left = mid+1
            else:
                if(target >= nums[mid] and target <= nums[right]):
                    left = mid+1
                else:
                    right = mid-1
            mid = left + (right-left)//2
        return -1
    #常规方法
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

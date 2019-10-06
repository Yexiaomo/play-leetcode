class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 设置两个索引, index1, index2分别跟随nums1, nums2
        # first,second 代表中间值和中间值前面的那个值
        first = second = 0
        index1 = index2 = 0
        len1 = len(nums1)
        len2= len(nums2)
        mid = (len1+len2) //2 +1
        for i in range(mid):
            second = first
            if( (index2 >= len2) or ((index1 < len1) and (nums1[index1] <= nums2[index2]))):
                first = nums1[index1]
                index1 += 1
            else:
                first = nums2[index2]
                index2 += 1
        
        if((len1+len2) % 2 == 0):
            return (first+second)/2
        else:
            return float(first)

''' #快速解法
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        mid = len(nums)//2
        if(len(nums)%2 == 0):
            return (nums[mid] + nums[mid-1])/2
        else:
            return float(nums[mid])
'''
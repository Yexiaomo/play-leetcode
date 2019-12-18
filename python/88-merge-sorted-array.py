class Solution:
    # 腾讯计划,改良版
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m+n-1
        m-=1
        n-=1
        while(m >= 0 and n >= 0):
            if(nums1[m] >= nums2[n]):
                nums1[index] = nums1[m]
                m-=1
            else:
                nums1[index] = nums2[n]
                n-=1
            index-=1
        # while(n>=0):
        #     nums1[index] = nums2[n]
        #     n-=1
        #     index-=1
        # while(m>=0):
        #     nums1[index] = nums1[m]
        #     m-=1
        #     index-=1
        # 上面的代码没有考虑到,如果nums1中元素还没有复制到目标数组,但是目标数组就是nums1就不用复制了
        # 所以只需要考虑nums2数组是不是已经拷贝完就可以了
        nums1[:n+1] = nums2[:n+1]


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #因为是在原数组的基础上修改,所以末尾开始
        #从大到小开始
        index = m+n-1
        m-=1
        n-=1
        while(m>=0 and n>=0):
            if(nums1[m] >= nums2[n]):
                nums1[index] = nums1[m]
                m-=1
            else:
                nums1[index] = nums2[n]
                n-=1
            index-=1
        while(m>=0):
            nums1[index] = nums1[m]
            index-=1
            m-=1
        while(n>=0):
            nums1[index] = nums2[n]
            index-=1
            n-=1

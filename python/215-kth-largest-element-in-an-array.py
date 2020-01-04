class Solution:
    #构建一个大小为k的大根堆
    #堆的最后一个元素就是第k大元素
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

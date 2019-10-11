class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max = 0
        while(l < r):
            h = height[l] if(height[l] <= height[r]) else height[r]
            tmp = h * (r-l)
            if(tmp > max):
                max = tmp
            if(height[l] <= height[r]):
                l += 1
            else:
                r -= 1
        return max
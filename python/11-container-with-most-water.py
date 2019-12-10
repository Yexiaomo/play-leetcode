class Solution:
    # 改良版
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        rst = 0
        while(l<r):
            if(height[l] < height[r]):
                rst = max(rst, (r-l)*height[l])
                l+=1
            else:
                rst = max(rst, (r-l)*height[r])
                r-=1
        return rst

    # 初版
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

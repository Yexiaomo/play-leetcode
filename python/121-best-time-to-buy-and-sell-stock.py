class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #寻找买入最小值和卖出最大值,需要注意卖出最大值一定位于买入最小值的后面
        min = 0
        max = 0
        ans = 0
        for i in range(1,len(prices)):
            #找买入最小值
            if(prices[i]<prices[min]):
                min = i
                #卖出最大值一定位于买入最小值的后面
                max = i
            #找卖出最大值
            if(prices[i]>=prices[max]):
                max = i
                ans = ans if(prices[max]-prices[min]<ans) else prices[max]-prices[min]
        return ans
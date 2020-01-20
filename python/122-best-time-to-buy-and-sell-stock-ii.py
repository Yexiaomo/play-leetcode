class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        inPrice = 0 #买入价格的索引
        ans = 0
        i = 1
        while(i<n):
            #寻找到当前价格比买入价格大的i
            if(prices[i] > prices[inPrice]):
                #如果当前价格大于买入价格
                #采用贪心算法,找到比当前卖出价格更大的卖出价格
                while(True):
                    #索引不能越界
                    if(i+1>=n): break
                    if(prices[i+1] > prices[i]):
                        i+=1
                    else:
                        break
                #找到所能找到的最大卖出价格,追加到结果中
                ans+=prices[i]-prices[inPrice]
            #更新
            inPrice = i
            i+=1
        return ans

    #和上面的基本一致
    def maxProfit(self, prices: List[int]) -> int:
        i, len_prices = 1, len(prices)
        if(len_prices < 2): return 0
        inPrice = prices[0]
        rst = 0
        while(i < len_prices):
            if(prices[i] > inPrice):
                while(True):
                    if(i+1 >= len_prices): break
                    if(prices[i+1] > prices[i]):
                        i+=1
                    else:
                        break                    
                rst += prices[i] - inPrice
            inPrice = prices[i]
            i+=1
        return rst

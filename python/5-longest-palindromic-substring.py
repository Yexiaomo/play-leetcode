class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        if(sLen == 0):
        	return ''
        # 初始化最长回文子串
        lp= s[0]
        lpLen  = 1
        # 采用中心扩散
        for i in range(sLen):
        	# 当前位置走两遍,看似两遍,实际上当前位置加0.5
        	pOdd, oddLen = self.__centerSpread(s, sLen, i, i)
        	pEven, evenLen = self.__centerSpread(s, sLen, i, i+1)

        	# 更新最长回文子串
        	curMaxSub = pOdd if(oddLen >= evenLen) else pEven
        	if(len(curMaxSub) > lpLen):
        		lpLen = len(curMaxSub)
        		lp = curMaxSub

        return lp
       
    def __centerSpread(self, s, sLen, l, r):
    	#如果左右两边相等,继续扩散
    	while(l>=0 and r<sLen and s[l] == s[r]):
    		l -= 1
    		r += 1
    	return s[l+1: r], r-l-1
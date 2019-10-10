class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x == None or x<0): return False
        x = str(x)
        xLen = len(x)
        for i in range(xLen//2):
            if(x[i] != x[xLen-i-1]):
                return False
        return True

# 改进后的代码, 人生苦短,我用Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return True if(x == x[::-1]) else False
    
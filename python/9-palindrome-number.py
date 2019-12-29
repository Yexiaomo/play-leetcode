class Solution:
    #反转整数后面一半就够了
    #负数,被十整除的数属于特殊情况
    def isPalindrome(self, x: int) -> bool:
        if(x < 0 or (x % 10 == 0 and x != 0)): return False
        xRight = 0
        while(xRight < x):
            xRight = x%10 + xRight*10
            x = x//10
        return xRight == x or xRight//10 == x
    
    #下面属于违规操作,使用了字符串
    # 改进后的代码, 人生苦短,我用Python
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return True if(x == x[::-1]) else False
    

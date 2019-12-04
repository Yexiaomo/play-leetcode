class Solution:
    def myAtoi(self, str: str) -> int:
        arrStr = str.split()
        # 判读是否字符串是否为空
        if(len(arrStr) == 0):
            return 0
        # 只判断第一个字符串
        numStr = ""
        s = arrStr[0]
        # 提取正负号
        if(s[0] in "+-0123456789"):
            numStr = numStr + s[0]
        else:
            return 0
        # 提取数字
        for j in range(1, len(s)):
            tmp = s[j]
            if(not tmp.isdigit()):
                break
            numStr = numStr + tmp
        # 判断是否提取到数字
        if(not numStr or numStr=='+' or numStr=='-'):
            return 0
        num = int(numStr)
        # 判断是否越界
        if(num >= 2**31):
            return (2**31-1)
        if(num < -2**31):
            return -2**31
        return num
    
''' 腾讯计划 2019/12/04
    def myAtoi(self, str: str) -> int:
        # 因为只需要判断字符串中第一个子串中的前整数部分
        subStr = str.split()
        if(subStr == []):
            return 0
        else:
            subStr = subStr[0]
        
        #提取正负号
        i = 0
        if(subStr[0] == '-'):
            i = 1
            flag = -1
        elif(subStr[0] == '+'):
            i = 1
            flag = +1
        elif(subStr[0].isdigit()):
            flag = +1
        else:
            return 0
        
        #获得数字子串
        ans = ''
        while(i<len(subStr)):
            if(subStr[i].isdigit()):
                ans += subStr[i]
                i+=1
            else:
                break
        if(ans == ''): return 0
        
        #对结果进行判别
        result = int(ans) * flag
        if(result >= 2**31):
            return (2**31-1)
        if(result < -2**31):
            return -2**31
        
        return result
'''

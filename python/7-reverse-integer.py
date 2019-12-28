class Solution:
    def reverse(self, x: int) -> int:
        # 结果变量
        rst = 0
        # 标志位,记录正负号
        flag = -1 if(x<0) else 1
        x = abs(x)
      	
        while(True):
            end = x%10
            rst = end + rst * 10
            x //= 10
            # 判断是否越界
            if(rst > 2147483647):
                return 0
            # 结束条件
            if(x==0):
                break
        # 返回
        return rst*flag

    # 膜拜大神
    def reverse(self, x: int) -> int:
    	# 将x转化为str,进行反转去除负号
        s = str(x)[::-1].rstrip("-")
        # 反转后的数是否越界
        if int(s) < 2**31:
            if x >= 0 :
                return int(s)
            else:
                return 0-int(s)
        return 0
    

    def reverse(self, x: int) -> int:
        if(x >= 0):
            rst = int(str(x)[::-1])
            return rst if(rst < (2**31)) else 0
        else:
            rst =  int('-' + str(x)[:0:-1])
            return rst if(rst > (-2**31)) else 0

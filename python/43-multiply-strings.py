class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len_num1 = len(num1)
        len_num2 = len(num2)
        sum = 0
        for n1 in range(len_num1):
            tmp = 0
            for n2 in range(len_num2):
                tmp = int(num1[n1]) * int(num2[n2]) + tmp*10
            sum = sum *10+ tmp
        return str(sum)
    
    # 腾讯计划2019/12/11
    def multiply(self, num1: str, num2: str) -> str:
        if(num1 == '0' or num2=='0'): return '0'
        len1 = len(num1)
        len2 = len(num2)
        rst = 0
        for i in range(len1):
            tmp = 0
            for j in range(len2-1, -1, -1):
                tmp =tmp + int(num1[i]) * int(num2[j]) * (10**(len2-j-1))
            rst = rst*10 + tmp
        return str(rst)

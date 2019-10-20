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
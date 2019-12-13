# 下面两种方法返回结果不一样
    # 如果测试用例为: s = " hello world "
    # 第一种方法返回: s = " olleh dlrow "
    # 第二种方法返回: s = "olleh dlrow"
# 不过这种方法都可以通过
class Solution:    
    
    # 腾讯计划2019/12/13
    def reverseWords(self, s: str) -> str:
        # 思路
        # 遍历整个字符串
        # 遇到非空格子串, 入栈
        # 遇到空字符串, 先清空栈,再空格加入到结果中
        # 继续循环直至结束
        # 返回之前判断栈是否为空
        len_s = len(s)
        if(len_s <= 1): return s
        stack = []
        rst = []
        for i in s:
            if(i == ' '):
                # 出栈,正好为子字符串的反转
                while(stack):
                    rst.append(stack.pop())
                rst.append(i)
            else:
                stack.append(i)
        while(stack):
            rst.append(stack.pop())
        return "".join(rst)

    # 腾讯精选
    def reverseWords(self, s: str) -> str:
        sArray = s.strip().split(' ')
        for i in range(len(sArray)):
            sArray[i] = sArray[i][::-1]
        return ' '.join(sArray)

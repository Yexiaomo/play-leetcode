class Solution:
    # 改良版2019/12/08
    def isValid(self, s: str) -> bool:
        if(len(s) %2 != 0): return False
        dict_brackets = {'(':')', '[':']', '{':'}'}
        stack = []
        for i in s:
            if(i in dict_brackets.keys()):
                stack.append(i)
            else:
                if(stack == [] or i != dict_brackets[stack.pop()]):
                    return False
        return not stack
    
    def isValid(self, s: str) -> bool:
        if(len(s) % 2 != 0):
            return False
        left_parenttheses = ['(','[','{']
        right_parenttheses = [')',']','}']
        s_stack = []
        for i in s:
            # 字符i为左括号, 入栈
            if(i in left_parenttheses):
                s_stack.append(i)
                continue
            # 字符i为右括号, 出栈与之判断
            if(i in right_parenttheses):
                tmp = " " if(len(s_stack) == 0) else s_stack.pop()
                if(tmp == left_parenttheses[right_parenttheses.index(i)]):
                    continue
                else:
                    return False
        return True if(s_stack == []) else False

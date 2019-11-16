class Solution:
    #位运算, 智商被按在地下摩擦
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n & (n-1)) == 0
    #从上至下
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if(n <= 0): return False
    #     while(n != 1):
    #         if(n%2 == 0):
    #             n = n//2
    #         else:
    #             return False
    #     return True
    # 从下至上
    # def isPowerOfTwo(self, n: int) -> bool:
    #      if(n == 1): return True
    #      if(n<1 or n%2 != 0): return False
    #      boundary = n//2
    #      cnt = 0
    #      while(cnt <= boundary):
    #         tmp = 2**cnt
    #         if(tmp == n):
    #             return True
    #         elif(tmp < n):
    #             cnt+=1
    #         else:
    #             break        
    #      return False

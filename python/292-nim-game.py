class Solution:
    def canWinNim(self, n: int) -> bool:
        # 推算一下
        # n<3必赢
        # n=4必输
        # n=5必赢
        # ....
        # 所以4的倍数必GG
        return n%4 != 0

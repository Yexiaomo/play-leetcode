class Solution:
    def reverseWords(self, s: str) -> str:
        sArray = s.strip().split(' ')
        for i in range(len(sArray)):
            sArray[i] = sArray[i][::-1]
        return ' '.join(sArray)

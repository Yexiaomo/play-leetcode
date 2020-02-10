/**最长回文子串
*方法: 中心扩散
*/
class Solution {
    
    public String longestPalindrome(String s) {
        //输入值判断
        if(s == null || s.length() < 1){
            return "";
        }
        //初始化
        int start = 0, end = 0;
        //遍历,每次前进 0.5step
        for(int i = 0; i < s.length(); i++){
            int lenOdd = centerSpread(s, i, i);
            int lenEven = centerSpread(s, i, i+1);
            //更新最长回文子串
            int len = Math.max(lenOdd, lenEven);
            if(len > end - start){
                start = i - (len-1)/2;
                end = i + len/2;
            }
        }
        return s.substring(start, end+1);
    }
    public int centerSpread(String s, int left, int right){
        while( left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
        }
        return right - left - 1;
    }
}

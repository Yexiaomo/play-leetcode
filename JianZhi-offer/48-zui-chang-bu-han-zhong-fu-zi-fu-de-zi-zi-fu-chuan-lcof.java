class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> dic = new HashMap<>();
        int i = -1, rst = 0;
        for(int j = 0; j < s.length(); j++){
            if(dic.containsKey(s.charAt[j]))
                i = Math.max(i, dic.get(s.charAt(j)));
            dic.put(s.charAt(j), j);
            rst = Math.max(rst, j - i);
        }
        return rst;
    }
}

class Solution {
    public char firstUniqChar(String s) {
        if(s == null)
            return ' ';
        if(s.length() == 1)
            return s.charAt(0);
        LinkedHashMap<Character, Integer> map = new LinkedHashMap<>();
        char c = ' ';
        for(int i = 0; i < s.length(); i++){
            c = s.charAt(i);
            map.put(c, map.getOrDefault(c,0)+1);
        }
        for(Character key : map.keySet()) {
            if (map.get(key) == 1) {
                return key;
            }
        }
        return ' ';
    }
}

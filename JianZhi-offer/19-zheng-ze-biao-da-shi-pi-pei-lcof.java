class Solution {
    public boolean isMatch(String s, String p) {
        if(s == null || p == null)
            return false;
        if(p.length() == 0 && s.length() != 0)
            return false;
        return matchCore(s, p, 0, 0);
    }
    boolean matchCore(String s, String p, int i, int j){
        if(i >= s.length() && j >= p.length()){
            return true;
        }
        if(j >= p.length()){
            return false;
        }
        boolean res = false;
        if(p.charAt(j) == '*'){
            //match more than one
            if(i < s.length() && 
               (p.charAt(j - 1) == s.charAt(i) || p.charAt(j - 1) == '.')){
                res = res || matchCore(s, p, i + 1, j);
                res = res || matchCore(s, p, i + 1, j + 1);
            }
            res = res || matchCore(s, p, i, j + 1);
        }else{
            if(i < s.length() && 
               (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.')){
                res = res || matchCore(s, p, i + 1, j + 1);
            }
            if(j < p.length() - 1 && p.charAt(j + 1) == '*'){
                res = res || matchCore(s, p, i, j + 2);
            }
        }
        return res;
    }
}

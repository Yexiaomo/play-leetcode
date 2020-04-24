class Solution {
    public String reverseLeftWords(String s, int n) {
        if(s == null || s == "")
            return "";
        //这两部分考虑了负数, 可惜我思考错了地方, 是不让用库函数
        // if(Math.abs(n) >= s.length())
        //     return s;
        // if(n < 0)
        //     n = s.length() + n;
        return s.substring(n) + s.substring(0, n);
    }
}

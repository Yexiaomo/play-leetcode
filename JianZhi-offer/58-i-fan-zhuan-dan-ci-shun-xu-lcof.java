class Solution {
    public String reverseWords(String s) {
        if(s == null || s.equals(""))
            return "";
        //分割字符串
        String[] arr = s.trim().split(" ");
        //翻转字符串数组
        StringBuilder rst = new StringBuilder();
        for(int i = arr.length -1; i >= 0; i--){
            if(arr[i].equals(""))
                continue;
            rst.append(arr[i]);
            if(i != 0)
                rst.append(" ");
        }
        return rst.toString();
    }
    //使用正则去除多余的空格, 巨慢
    // public String reverseWords(String s) {
    //     if(s == null || s.equals(""))
    //         return "";
    //     //分割字符串
    //     String[] arr = s.trim().split(" +");
    //     //翻转字符串数组
    //     StringBuilder rst = new StringBuilder();
    //     for(int i = arr.length -1; i >= 0; i--){
    //         if(i != 0){
    //             rst.append(arr[i] + " ");
    //         }else{
    //             rst.append(arr[i]);
    //         }
    //     }
    //     return rst.toString();
    // }
}

class Solution {
    //方法①:构建个StringBuilder对象
    // public String replaceSpace(String s) {  
    //    StringBuilder rst = new StringBuilder();
    //    for(Character c : s.toCharArray()){
    //        if(c == ' '){
    //            rst.append("%20");
    //        }else{
    //            rst.append(c);
    //        }
    //    }
    //    return rst.toString();
    // }

    //方法②: char数组
    public String replaceSpace(String s) {  
        char[] s1 = s.toCharArray();
        int cnt = 0;
        for(char c : s1){
            if(c == ' '){
                cnt++;
            }
        }
        char[] rst = new char[s1.length + cnt*2];
        int i = 0;
        for(char c : s1){
            if(c == ' '){
                rst[i++] = '%';
                rst[i++] = '2';
                rst[i++] = '0';
            }else{
                rst[i++] = c;
            }
        }
        return new String(rst);
    }
}
class Solution {
    public int strToInt(String str) {
        if(str == null) return 0;
        char[] cArr = str.trim().toCharArray();
        if(cArr.length == 0) return 0;
        
        int i = 1, sign = 1;
        long rst = 0;

        if(cArr[0] == '-'){
            sign = -1;
        }else if(cArr[0] != '+'){
            i = 0;
        }

        for(int j = i; j < cArr.length; j++){
            if(cArr[j] < '0' || cArr[j] > '9') break;
            rst = rst*10 + (cArr[j] - '0');
            if(rst > Integer.MAX_VALUE)
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
        }

        return sign * (int) rst;
    }
}

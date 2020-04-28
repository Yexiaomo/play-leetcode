class Solution {
    public int findNthDigit(int n) {
        if(n < 9)
            return n;
        int digit = 1;//位数
        long start = 1;//数字起始位置
        long count = 9;//当前位数所含数字的数量
        //得到n所在的位数
        while(n > count){
            n -= count;

            digit++;
            start *= 10;
            count = 9 * digit * start;
        }
        //确定n所在的 数字 是几
        long num = start + (n-1) / digit;
        return Long.toString(num).charAt( (n-1) % digit) - '0';

    }
}

class Solution {
    //不考虑大数问题
    public int[] printNumbers(int n) {
        int num = (int) Math.pow(10, n) - 1;
        int[] rst = new int[num];
        for(int i = 0; i < num; ){
            rst[i] = ++i;
        }
        return rst;
    }
}

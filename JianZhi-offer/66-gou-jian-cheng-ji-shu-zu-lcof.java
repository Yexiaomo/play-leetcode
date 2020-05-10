class Solution {
    public int[] constructArr(int[] a) {
        if(a == null || a.length == 0)
            return new int[0];

        int len = a.length;
        int[] b = new int[len];
        //统计当前下标左边的乘积
        b[0] = 1;
        for(int i = 1; i < len; i++)
            b[i] = b[i-1] * a[i-1];
        //统计当前下标右边的乘积
        //b[i] = 当前下标左边乘积 * 当前下标右边乘积;
        for(int i = len-2, tmp = 1; i >= 0; i--){
            tmp *= a[i+1];
            b[i] *= tmp;
        }

        return b;
    }
}

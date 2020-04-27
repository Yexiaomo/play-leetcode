class Solution {
    public double[] twoSum(int n) {
        if(n == 0)
            return new double[0];
        int[] dp = new int[6*n + 1];
        double[] rst = new double[5*n + 1];
        double cnt = Math.pow(6, n);
        //设定初始状态
        for(int i = 1; i <= 6; i++)
            dp[i] = 1;
        //开始迭代
        for(int i = 2; i <= n; i++){
            for(int j = 6 * i; j >= i; j--){
                //因为是从后往前逐个累加，在加到当前点数时，必须把原先存放的n-1个骰子的数据置0，否则累加出错。
                dp[j] = 0;
                for(int cur = 1; cur <= 6; cur++){
                    //如果不加此判据，会取到n-2个骰子的数据，此时可认为是“脏数据”，会导致累加出错。从实际情况来分析，n-1个骰子的最小值就是n-1，不会比这再小，因此此处的判据是 i-1，而不是0
                    if(j-cur < i-1)
                        break;
                    dp[j] += dp[j-cur];
                }
            }
        }
        for(int i = 0; i < dp.length; i++){
            System.out.print(dp[i]+",");
        }
        //计算概率
        for(int i = 0; i < rst.length; i++){
            rst[i] = dp[i+n] / cnt;
        }
        return rst;
    }
}

class Solution {
    public int nthUglyNumber(int n) {
        if(n < 1)
            return 0;
        int[] dp = new int[n];
        dp[0] = 1;
        //三个指针
        int p2 = 0, p3 = 0, p5 = 0;
        for(int i = 1; i < n ; i++){
            int n2 = dp[p2] * 2,  n3 = dp[p3] * 3,  n5 = dp[p5] * 5;
            dp[i] = Math.min(n2, Math.min(n3, n5));
            if(dp[i] == n2) p2++;
            if(dp[i] == n3) p3++;
            if(dp[i] == n5) p5++;
        }
        return dp[n-1];
    }
}

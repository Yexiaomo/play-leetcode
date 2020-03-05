class Solution {
    public int numWays(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;
        int a = 1, b = 2;
        int ans = 1;
        for(int i = 3; i <= n; i++){
            ans = a + b;
            if(ans >= 1000000007){
                ans = ans - 1000000007;
            }
            a = b;
            b = ans;
        }
        return ans;
    }
}

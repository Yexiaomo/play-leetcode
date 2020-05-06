class Solution {
    public int lastRemaining(int n, int m) {
        // int ans = 0;
        // for(int i = 2; i <= n; i++){
        //     ans = (ans + m) % i;
        // }
        // return ans;
        int ans = 0, i = 2;
        while(i <= n)
            ans = (ans + m) % i++;
        return ans;
    }
}

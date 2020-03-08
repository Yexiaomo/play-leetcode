class Solution {
    private int rst, m, n, k;
    private boolean[][] visited;
    public int movingCount(int m, int n, int k) {
        this.visited = new boolean[m][n];
        this.rst = 0;
        this.m = m;
        this.n = n;
        this.k = k;
        dfs(0, 0);
        return rst;
    }
    private void dfs(int i, int j){
        if(i<0 || i>=m || j<0 || j>=n || compareK(i, j) || visited[i][j]) return ;
        rst++;
        visited[i][j] = true;
        dfs(i-1, j);
        dfs(i+1, j);
        dfs(i, j+1);
        dfs(i, j-1);
    }
    private boolean compareK(int a, int b){
        int sum = 0;
        while(a!=0 || b!=0){
            sum += a%10 + b%10;
            a = a/10;
            b = b/10;
        }
        return sum>k;
    }
}

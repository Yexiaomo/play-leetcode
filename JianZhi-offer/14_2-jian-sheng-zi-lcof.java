class Solution {
    public int cuttingRope(int n) {
        return (n<=3)? (n-1) : (int)process(n);
    }
    public long process(int n){
        return (n>4) ? (process(n-3)*3)%1000000007 : n;
    }
}

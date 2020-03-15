class Solution {
    public double myPow(double x, int n) {
        if(x == 0.0 && n < 0) return 0.0;
        long exponent = n;
        if(n < 0){
            exponent = -exponent;
            x = 1 / x;
        }
        double rst = 1.0;
        while(exponent != 0){
            if( (exponent & 1) == 1)
                rst *= x;
            x *= x;
            exponent>>=1;
        }
        return rst;
    }
}

class Solution {
    public int cuttingRope(int n) {
        if(n <= 1) return 0;
        if(n == 2) return 1;
        if(n == 3) return 2;
        //尽可能的剪更多长度为3的绳子
        int timeOf3 = n/3;
        int last = n%3;
        //注意当最后的长度剩下为1时, 需要和前面的一个3合并, 因为 2*2 > 3*1
        if(n%3 == 0){
            return (int) Math.pow(3, timeOf3);
        }else if(n%3 == 1){
            return (int) Math.pow(3, --timeOf3) * 4;
        }else{
             return (int) Math.pow(3, timeOf3) * 2;
        }
    }
}

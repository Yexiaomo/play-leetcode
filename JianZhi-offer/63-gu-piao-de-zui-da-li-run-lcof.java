class Solution {
    public int maxProfit(int[] prices) {
        int inPrice = Integer.MAX_VALUE;
        int rst = 0;
        for(int price : prices){
            inPrice = Math.min(inPrice, price);
            rst = Math.max(rst, price - inPrice);
        }
        return rst;
    }
}

class Solution {
    public int add(int a, int b) {
        while(b != 0){ //无进位
            int plus = a ^ b; //求无进位的和
            b = (a & b) << 1; //求进位
            a = plus; //更新结果
        }
        return a;
    }
}

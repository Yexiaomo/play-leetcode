class Solution {
    public int singleNumber(int[] nums) {
        if(nums == null || nums.length < 4)
            return 0;
        //统计32位二进制数每位上的和
        int[] bitSum = new int[32];
        for(int n : nums){
            int bitMask = 1;
            for(int i = 31; i > 0; i--){
                int bitValue = n & bitMask;
                if(bitValue != 0)
                    bitSum[i] += 1;
                bitMask <<= 1;
            }
        }
        //计算结果
        int rst = 0;
        for(int b : bitSum){
            rst <<= 1;
            rst += b % 3;
        }
        return rst;
    }
}

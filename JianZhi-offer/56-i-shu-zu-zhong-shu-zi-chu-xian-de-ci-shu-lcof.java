class Solution {
    public int[] singleNumbers(int[] nums) {
        int[] rst = {0,0};
        int tmp = 0;
        for(int n : nums)
            tmp ^= n;
        int mask = tmp & -tmp;
        // for(int n : nums){
        //     if((n & mask) == 0)
        //         rst[0] ^= n;
        //     else
        //         rst[1] ^= n;
        // }
        // return rst;
        //看了提交时间为1ms的结果, 将以上代码进行优化
        for(int n : nums)
            if((n & mask) == 0)
                rst[0] ^= n;
        rst[1] = rst[0] ^ tmp;
        return rst;
    }
}

class Solution {
    public int maxSubArray(int[] nums) {
        if(nums == null || nums.length == 0)
            return 0;
        int rst = nums[0];
        int ans = nums[0];
        for(int i = 1; i < nums.length; i++){
            ans = Math.max(nums[i], ans + nums[i]);
            rst = Math.max(rst, ans);
        }
        return rst;
    }
}

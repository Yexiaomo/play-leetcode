class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] rst = new int[2];
        int left = 0, right = nums.length-1;
        int ans;
        while(left < right){
            ans = nums[left] + nums[right];
            if(ans == target){
                rst[0] = nums[left];
                rst[1] = nums[right];
                break;
            }else if(ans > target){
                --right;
            }else{
                ++left;
            }
        }
        return rst;
    }
}

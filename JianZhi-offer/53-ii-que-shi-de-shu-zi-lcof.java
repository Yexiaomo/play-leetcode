class Solution {
    public int missingNumber(int[] nums) {
        int left = 0, right = nums.length-1;
        int mid;
        while(left < right){
            mid = (left + right) / 2;
            if(nums[mid] <= mid){
                left = mid+1;
            }else{
                right = mid;
            }
        }
        //最后判断一下数组是否全部有序, 全部有序返回n
        return left == nums.length - 1 && nums[left] == left ? left + 1 : left;
    }
}

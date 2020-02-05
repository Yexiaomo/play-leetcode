class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> ansMap = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int tmp = target - nums[i];
            if(ansMap.containsKey(tmp)){
                return new int[] {ansMap.get(tmp), i};
            }else{
                ansMap.put(nums[i], i);
            }
        }
        //--我以前用的是这种方法--
        //return null;
        //leetcode官网用的是这种带有提示的返回值
        throw new IllegalArgumentException("No two sum solution!");
    }
}

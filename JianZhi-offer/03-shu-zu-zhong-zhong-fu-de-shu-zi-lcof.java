class Solution {
    //方法①: 使用集合法, 空间复杂度高
    // public int findRepeatNumber(int[] nums) {
    //     Set ansSet = new HashSet();
    //     for(int n : nums){
    //         if( ansSet.contains(n) ){
    //             return n;
    //         }else{
    //             ansSet.add(n);
    //         }
    //     }
    //     return -1;
    // }
    //方法②: 使用原地排序法
    public int findRepeatNumber(int[] nums) {
        int tmp;
        for(int i = 0; i < nums.length; i++){
            while(nums[i] != i){
                if(nums[i] == nums[nums[i]]){
                    return nums[i];
                }
                // tmp = nums[i];
                // nums[i] = nums[tmp];
                // nums[tmp] = tmp;
                //利用位运算进行交换
                nums[i] = nums[i] ^ nums[nums[i]];
                nums[nums[i]] = nums[i] ^ nums[nums[i]];
                nums[i] = nums[i] ^ nums[nums[i]];
            }
        }
        return -1;
    }
}

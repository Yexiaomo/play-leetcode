class Solution {
    public int[] exchange(int[] nums) {
        /*头尾指针: 头指针用来找偶数, 尾指针用来找奇数
        */
        if(nums == null || nums.length <= 1)
            return nums;
        int head = 0, tail = nums.length - 1;
        while(head < tail){
            while(head<tail && nums[head] % 2 != 0){
                head++;
            }
            while(head<tail && nums[tail] % 2 == 0){
                tail--;
            }
            if(head < tail){
                int tmp = nums[head];
                nums[head] = nums[tail];
                nums[tail] = tmp;
            }
        }
        return nums;
    }
}

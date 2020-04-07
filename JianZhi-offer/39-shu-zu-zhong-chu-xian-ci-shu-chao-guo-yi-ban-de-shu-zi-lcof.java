class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        int rst = 0;
        for(int n : nums){
            if(count == 0)
                rst = n;
            count += (n == rst ? 1 : -1);
        }
        return rst;
    }
}

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int len = nums.length;
        if(len == 0)
            return new int[0];
        int[] rst = new int[len-k+1];
        int maxIdx = -1, max = Integer.MIN_VALUE;
        for(int i = 0; i < len - k + 1; i++){
            //判断最大值索引是否还在滑动窗口内
            if(maxIdx >= i){
                //存在的话, 只需要和新进入滑动窗口的值判断
                if(nums[i+k-1] > max ){
                    maxIdx = i+k-1;
                    max = nums[maxIdx];
                }
            }else{
                //最大值不在窗口, 需重新查找
                maxIdx = i;
                for(int j = i+1; j < i+k; j++){
                    if(nums[j] > nums[maxIdx]){
                        maxIdx = j;
                    }
                }
                max = nums[maxIdx];
            }
            rst[i] = max;
        }
        return rst;
    }
}

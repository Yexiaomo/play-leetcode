/*https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/gui-bing-pai-xu-duo-liang-xing-dai-ma-by-__sun*/
class Solution {
    private int rst = 0;
    public int reversePairs(int[] nums) {
        int len = nums.length;
        int[] copy = new int[len];
        for(int i = 0; i < len; i++)
            copy[i] = nums[i];
        
        //归并排序
        mergeSort(copy, 0, len-1);
        return rst;
    }
    public void mergeSort(int[] nums, int left, int right){
        if(left >= right)
            return;
        
        int mid = (left + right) / 2;
        mergeSort(nums, left, mid);
        mergeSort(nums, mid+1, right);
        
        int l = left, r = mid + 1, cur = 0;
        int[] tmp = new int[right - left + 1];

        while(l <= mid && r <= right){
            if(nums[l] <= nums[r]){
                tmp[cur] = nums[l++];
                rst += r - (mid + 1);
            }else{
                tmp[cur] = nums[r++];
            }
            cur++;
        }

        while(l <= mid){
            tmp[cur++] = nums[l++];
            rst += r - (mid + 1);
        }
        while(r <= right){
            tmp[cur++] = nums[r++];
        }

        for(int i = 0; i < tmp.length; i++)
            nums[left+i] = tmp[i];
    }
}

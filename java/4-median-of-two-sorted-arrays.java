class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        //分别为两个数组的索引
        int index1 = 0, index2 = 0;
        //因为不知道两个数组长度之和为奇为偶,所以中位数要保存两个
        int fast = 0, slow = 0;
        //找中位数只需要遍历一般就行了
        int lens = nums1.length + nums2.length;
        int mid = lens / 2 + 1;
        for(int i = 0; i < mid; i++){
            //更新slow的值
            slow = fast;
            if( (index2 >= nums2.length)  || ( (index1 < nums1.length) && (nums1[index1] <= nums2[index2]))) {
                fast = nums1[index1];
                index1++;
            }else{
                fast = nums2[index2];
                index2++;
            }
        }
        if(lens % 2 == 0){
            return (fast+slow)/2.0;
        }else{
            return fast*1.0;
        }
    }
}

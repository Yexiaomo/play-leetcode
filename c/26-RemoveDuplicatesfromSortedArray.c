//26. Remove Duplicates from Sorted Array
//题目描述（https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/）
//因为数组有序，所以还是可以用双指针就行了2019/2/3
int removeDuplicates(int* nums, int numsSize) {
    if(nums == NULL || numsSize <= 0)
        return 0;
    int i = 0, j = 1;
    for(; j < numsSize;){
        if(nums[j] == nums[i]){
            j++;
        }else{
            nums[++i] = nums[j++];
        }
    }
    return ++i;
}
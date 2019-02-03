//27. Remove Element
//题目描述（https://leetcode-cn.com/problems/remove-element/）
//因为数组有序，所以还是可以用双指针就行了2019/2/3
int removeElement(int* nums, int numsSize, int val) {
    if(nums==NULL || numsSize<=0 )
        return 0;
    int i = 0;
    int j = i;
    for(; j < numsSize; j++){
        if(nums[j] != val){
            nums[i++] = nums[j];
        }
    }
    return i;
}
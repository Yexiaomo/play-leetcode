//80. Remove Duplicates from Sorted Array II
//题目描述（https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/）

//自己没想出来，把自己绕死了。看了别人的发现自己真是笨，思想非得在一个数组上，完全可以将一个数组看成两个数组，互不干扰
//
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
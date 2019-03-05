//75. 颜色分类
//题目描述（https://leetcode-cn.com/problems/sort-colors/）

//超垃圾的算法，应该使用三路快排   3/5/2019
//下面用的是计数排序
void sortColors(int* nums, int numsSize) {
    if(numsSize <=1 || nums==NULL)
        return ;
    int i;
    int n0, n1, n2;
    for(i = 0, n0=0,n1=0,n2=0; i < numsSize; i++){
        if(nums[i] == 0)
            n0++;
        else if(nums[i] == 1)
            n1++;
        else
            n2++;
    }
    i = 0;
    while(i<n0)
        nums[i++] = 0;
    while(i<(n1+n0))
        nums[i++] = 1;
    while(i<(n1+n0+n2))
        nums[i++] = 2;
    return ;
}
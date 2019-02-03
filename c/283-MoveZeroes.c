//283. Move Zeroes
//题目描述（https://leetcode-cn.com/problems/move-zeroes/）

//显然这是最笨的方法，为啥不动动脑子思考一下，要挪动0，也不需要使用交换啊，直接赋值不就行了，神经病一样我。
// void moveZeroes(int* nums, int numsSize) {
//     int i, j, temp, n;
//     for(i = 0, j = 1, n = 0; i<numsSize-1 && j<numsSize; i++){
//         if(nums[i] == 0){
//             for(j=i+1; j<numsSize; j++){
//                 if(nums[j]!=0){
//                     nums[i] = nums[j];
//                     nums[j] = 0;
//                  break;
//                 }
//             }
//             n++;
//         }
//     }
// }
//时间复杂度为O(n),操作n次
void moveZeroes(int* nums, int numsSize) {
    int i, j;
    for(i = 0, j = 0; j < numsSize; j++){
        if(nums[j]!= 0){
            nums[i++] = nums[j];
        }
    }
    while(i<numsSize)
        nums[i++] = 0;
}


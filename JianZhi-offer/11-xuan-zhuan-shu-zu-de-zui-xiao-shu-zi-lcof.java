class Solution {
    public int minArray(int[] numbers) {
        if(numbers == null || numbers.length < 1)
            return -1;
        int left = 0, right = numbers.length-1;
        while(left < right){
            // int mid = ((right - left) / 2) + left;
            int mid = ((right - left) >> 1) + left;
            if(numbers[mid] < numbers[right]){
                right = mid;
            }else if(numbers[mid] > numbers[right]){
                left = mid+1;
            }else{
                //到这一步说明, left, mid, right三值重复
                --right;
            }
        }
        return numbers[left];
    }
}

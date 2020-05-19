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
                //如果走到这一步, 说明left, mid, right相同
                //如剑指offer书上提到的[1,0,1,1,1]或者[1,1,1,0,1]
                --right;
            }
        }
        return numbers[left];
    }
}

class Solution {
    public int[] getLeastNumbers(int[] arr, int k) {
        if(k <= 0)
            return new int[0];
        if(arr == null || arr.length == 0 || arr.length <= k)
            return arr;
        //将数组的前四个数,排序存入到结果数组中
        int[] rst = new int[k];
        for(int i = 0; i < k; i++)
            rst[i] = arr[i];
        int maxIndex = getMaxIndex(rst, 0);
        for(int i = k; i < arr.length; i++){
            if(arr[i] < rst[maxIndex]){
                rst[maxIndex] = arr[i];
                maxIndex = getMaxIndex(rst, maxIndex);
            }
        }
        return rst;
    }
    /*
    *@获取数组中最大值的索引
    */
    public int getMaxIndex(int[] array, int index){
        for(int i = 1; i < array.length; i++)
            if(array[i] > array[index]){
                index = i;
        
        return index;
    }
}

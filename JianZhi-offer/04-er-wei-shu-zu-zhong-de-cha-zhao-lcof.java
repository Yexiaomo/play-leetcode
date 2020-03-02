class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if(matrix==null || matrix.length==0)
            return false;
        int i = matrix.length - 1, j = 0;
        while(i > -1 && j < matrix[0].length){
            if(matrix[i][j] > target){
                i-=1;
            }else if(matrix[i][j] < target){
                j+=1;
            }else{
                return true;
            }
        }
        return false;
    }
}

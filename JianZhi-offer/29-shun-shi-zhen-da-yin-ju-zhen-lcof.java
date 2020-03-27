class Solution {
    public int[] spiralOrder(int[][] matrix) {
        if(matrix == null || matrix.length == 0)
            return new int[0];
        int[] rst = new int[matrix.length * matrix[0].length];
        int left = 0, right = matrix[0].length-1;
        int up = 0, down = matrix.length-1;
        int index = 0;
        while(left <= right && up <= down){
            for(int i = left; i <= right; ++i){
                rst[index++] = matrix[up][i];
            }
            for(int i = up+1; i <= down; ++i){
                rst[index++] = matrix[i][right];
            }
            if(up != down){
                for(int i = right-1; i >= left; --i){
                    rst[index++] = matrix[down][i];
                }
            }
            if(left != right){
                for(int i = down-1; i > up; --i){
                    rst[index++] = matrix[i][left];
                }
            }
            left++;
            right--;
            up++;
            down--;
        }
        return rst;
    }
}

class Solution {
    public boolean exist(char[][] board, String word) {
        char[] target = word.toCharArray();
        for(int i = 0; i < board.length; ++i){
            for(int j = 0; j < board[0].length; ++j){
                if(dfs(board, target, i, j, 0))
                    return true;
            }
        }
        return false;
    }

    public boolean dfs(char[][] board, char[] target, int i, int j, int k){
        if( i>=board.length || i<0 || j>=board[0].length || j<0 
                                   || board[i][j]!=target[k]){
            return false;
        }
        if(k == target.length-1) return true;
        char tmp = board[i][j];
        board[i][j] = '/';
        boolean res = dfs(board, target, i+1, j, k+1)
                      || dfs(board, target, i-1, j, k+1)
                      || dfs(board, target, i, j+1, k+1)
                      || dfs(board, target, i, j-1, k+1);
        board[i][j] = tmp;
        return res;
    }
}

class Solution {
    public boolean isStraight(int[] nums) {
        //遍历这5张牌,找到最小值, 最大值,和大小王的个数
        int max = -1, min = 14, cnt = 0;
        boolean[] map = new boolean[14];
        for(int n : nums){
            if(n == 0){
                cnt++;
            }else{
                if(map[n] == true)
                    return false;
                else
                    map[n] = true;
                
                if(n < min) min = n;
                if(n > max) max = n;
            }
        }
        return cnt >= 4 || max - min <= 4;
    }
}
/*
https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
*/
class Solution {
    public int[][] findContinuousSequence(int target) {
        int i = 1;
        int j = 1;
        int sum = 0;
        List<int[]> rst = new ArrayList<>();
        while(i <= target/2){
            if(sum < target){
                //有边界移动
                sum += j;
                j++;
            }else if(sum > target){
                sum -= i;
                i++;
            }else{
                //记录结果
                int[] ans = new int[j-i];
                for(int k = i; k < j; k++)
                    ans[k-i] = k;
                rst.add(ans);
                sum-=i;
                i++;
            }
        }
        return rst.toArray(new int[rst.size()][]);
    }
}

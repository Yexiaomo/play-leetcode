class Solution {
    public String minNumber(int[] nums) {
        if(nums == null || nums.length == 0)
            return "";
        String[] strNums = new String[nums.length];
        StringBuilder rst = new StringBuilder();
        //1. 将数字数组转换为字符串数组
        for(int i = 0; i < nums.length; i++)
            strNums[i] = String.valueOf(nums[i]);
        //2. 字符串数组排序
        Arrays.sort(strNums, (x, y)->(x + y).compareTo(y + x));
        //3. 拼接结果
        for(String s : strNums)
            rst.append(s);
        return rst.toString();
    }
}

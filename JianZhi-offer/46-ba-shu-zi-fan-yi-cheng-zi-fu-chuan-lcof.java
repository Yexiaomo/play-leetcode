class Solution {
    public int translateNum(int num) {
        if(num <= 9)
            return 1;
        //先取后两位
        int ba = num % 100;
        if(ba <= 9 || ba >= 26){
            return translateNum(num / 10);
        }else{
            return translateNum(num/10) + translateNum(num/100);
        }
    }
}

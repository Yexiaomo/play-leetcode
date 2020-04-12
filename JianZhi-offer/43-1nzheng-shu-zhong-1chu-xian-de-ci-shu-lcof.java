/*
解析
需要通过找规律来分析。
假设我们对5014这个数字求解。
（1）个位上1出现的个数：记高位为high=501，当前位为cur=4。
那么高位从0~500变化的过程中，每一个变化中1只出现1次，即（高位1）这样的数字；
高位是501时，因为当前位是4，所以1只能出现一次，即5011。
所以总共出现的次数为high*1+1=502。
（2）十位1出现的个数：记高位high=50，当前位为cur=1，低位为low=4。
那么高位从0~ 49变化的过程中，每一个变化中1出现10次，即（高位10）~（高位19）这样的数字；
高位为50的时候，因为当前位是1，所以我们要看低位来决定出现的次数，因为低位为4，所以此时出现5次，即5010~5014这样的数字。
所以总共出现的次数为high*10+4=504。
（3）百位1出现的个数：记高位high=5，当前位cur=0，低位为low=14。
那么高位从0~ 4的过程中，每一个变化1出现100次，即（高位100）~（高位199）这样的数字；
高位为5的时候，因为当前位为0，所以不存在出现1的可能性。
所以总共出现的次数为high*100+0=500。
（4）千位1出现的次数：记高位high=0，当前位cur=5，低位low=014。
那么因为没有高位所以直接看当前位，因为当前位为5，所以1出现的次数为1000，即1000~1999这样的数字。
所以总共出现的次数为high*1000+1000=1000。
综上，最终的结果将每个位置出现1的次数累加即可。

结论
我们假设高位为high，当前位为cur，低位为low，i代表着需要统计的位置数（1对应个位，10对应十位，100对应百位），则对每一位的个数count有：
cur=0,count = high*i;
cur=1,count=high*i+low+1;
cur>1,count=high*i+i
最终累加所有位置上的个数即最终答案。

作者：lu-yang-shan-yu
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/c-cong-ge-wei-bian-li-dao-zui-gao-wei-yi-ci-qiu-ji/
来源：力扣（LeetCode）
*/
class Solution{
    public int countDigitOne(int n){
        int count = 0;
        long i = 1;
        while(n / i != 0){
            long high = n / (10 * i);
            long low = n - (n / i) * i;
            long cur = (n / i) % 10;
            if(cur == 0){
                count += high * i;
            }else if(cur == 1){
                count += high * i + low + 1;
            }else{
                count += high * i + i;
            }
            i *= 10;
        }
        return count;
    }
}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if(ans.get(tmp) != None):
                if(i != ans[tmp]):
                    return [ans[tmp], i]
            ans[nums[i]] = i
        return None
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=nums[0]
        n=len(nums)
        max_sum=nums[0]
        for i in nums[1:]:
            cur_sum=max(cur_sum+i,i)
            max_sum=max(cur_sum,max_sum)
        return max_sum

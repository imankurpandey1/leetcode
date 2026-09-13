class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_prod=max_prod=min_prod=nums[0]
        for num in nums[1:]:
            temp_max=max(max_prod*num,num,min_prod*num)
            min_prod=min(max_prod*num,num,min_prod*num)
            max_prod=temp_max
            curr_prod=max(curr_prod,max_prod)
        return curr_prod
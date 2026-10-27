class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        seen={}
        for i in range(n):
            req=target-nums[i]
            if req in seen:
                return [seen[req],i]
            seen[nums[i]]=i
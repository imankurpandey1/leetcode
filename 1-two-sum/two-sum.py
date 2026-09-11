class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
        n=len(nums)
        dict1={}
        for i in range(n):
            req=target-nums[i]
            if req in dict1:
                return [dict1[req],i]
            dict1[nums[i]]=i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i in range(len(nums)):
            req=target-nums[i]
            if req in visited:
                return(visited[req],i)
            visited[nums[i]]=i
        return visited
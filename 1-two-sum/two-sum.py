from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            required = target - nums[i]

            if required in visited:
                return [visited[required], i]

            visited[nums[i]] = i
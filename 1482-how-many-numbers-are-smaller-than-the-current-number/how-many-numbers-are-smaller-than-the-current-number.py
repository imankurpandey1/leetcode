class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        m=len(nums)
        for i in range (m):
            count=0
            for j in range (m):
                if nums[i]>nums[j]:
                    count+=1
                    
            result.append(count)
        return result
        
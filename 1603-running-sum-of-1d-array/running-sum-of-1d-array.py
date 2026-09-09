class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        running_sum=[]
        total=0
        for i in range (n):
            total=total+nums[i]
            
            running_sum.append(total)
        return running_sum


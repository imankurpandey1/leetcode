class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        cl=nums[0]
        for num in nums:
            if abs(num)<abs(cl):
                cl=num
            elif abs(num)==abs(cl):
                cl=max(cl,num)
        return cl
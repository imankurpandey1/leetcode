class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        j=1
        if n<=2:
            return n
        for i in range(2,n):
            if nums[i]!=nums[j-1]:
                j+=1
                nums[j]=nums[i]
        return j+1



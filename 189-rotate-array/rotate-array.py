class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def rev(start:int,end:int)->none:
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
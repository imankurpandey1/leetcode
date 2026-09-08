class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        for i in range(len(candies)):
            max_c=max(candies)
            if candies[i]+extraCandies>=max_c:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
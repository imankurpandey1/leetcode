class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        ans=0
        while temp>0:
            val=temp%10
            temp//=10
            if num%val==0:
                ans+=1
        return ans
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans=0
        temp=x
        while temp>0:
            val=temp%10
            temp//=10
            ans=ans*10+val
        if ans==x:
            return(True)
        else:
            return(False)
        
        
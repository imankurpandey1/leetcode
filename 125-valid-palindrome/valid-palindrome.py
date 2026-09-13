class Solution:
    def isalphanum(self,s):
        s=s.lower()
        st=ord(s)
        if 97<=st<=122 or 65<=st<=90 or 48<=st<=57:
            return True

        return False
    def isPalindrome(self, s: str) -> bool:
        left=0
        s=s.lower()
        right=len(s)-1
        while left<right:
            
            if not self.isalphanum(s[left]):
                left+=1
                
            elif not self.isalphanum(s[right]):
                right-=1
            elif s[left]!=s[right]:
                return False
                
            
            elif s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
                
        return True



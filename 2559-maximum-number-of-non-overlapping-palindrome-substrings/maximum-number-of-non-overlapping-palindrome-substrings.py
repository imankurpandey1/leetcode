class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        i = 0
        
        while i <= n - k:
            if s[i:i+k] == s[i:i+k][::-1]:
                count += 1
                i += k
            elif i + k <= n and s[i:i+k+1] == s[i:i+k+1][::-1]:
                count += 1
                i += k + 1
            else:
                i += 1
                
        return count
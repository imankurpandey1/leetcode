class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip().split()
        rev=s.reverse()
        return " ".join(s)


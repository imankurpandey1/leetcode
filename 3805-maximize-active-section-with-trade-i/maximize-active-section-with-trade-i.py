class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ans = s.count('1')
        pre = float('-inf')
        mx = 0
        i = 0
        n = len(s)

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            cur = j - i

            if s[i] == '0':
                mx = max(mx, pre + cur)
                pre = cur

            i = j

        return ans + mx
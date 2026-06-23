class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def calc(s1, d1, s2, d2):
            first_end = min(s + d for s, d in zip(s1, d1))
            ans = float('inf')
            
            for s, d in zip(s2, d2):
                ans = min(ans, max(first_end, s) + d)
            
            return ans

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )
from bisect import bisect_right

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def solve(a, b, c, d):
            rides = sorted(zip(c, d))
            n = len(rides)

            pre = [0] * n
            pre[0] = rides[0][1]
            for i in range(1, n):
                pre[i] = min(pre[i - 1], rides[i][1])

            suf = [0] * n
            suf[-1] = rides[-1][0] + rides[-1][1]
            for i in range(n - 2, -1, -1):
                suf[i] = min(suf[i + 1], rides[i][0] + rides[i][1])

            starts = [x for x, _ in rides]
            ans = float('inf')

            for s, t in zip(a, b):
                finish = s + t
                idx = bisect_right(starts, finish)

                if idx:
                    ans = min(ans, finish + pre[idx - 1])

                if idx < n:
                    ans = min(ans, suf[idx])

            return ans

        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration)
        )
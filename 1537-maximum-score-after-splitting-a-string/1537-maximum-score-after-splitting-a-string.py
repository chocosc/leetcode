class Solution:
    def maxScore(self, s: str) -> int:
        ans = []
        for i in range(1,len(s)):
            l = s[:i]
            r = s[i:]
            ans.append(l.count('0') + r.count('1'))
            
        return max(ans)
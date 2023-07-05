class Solution:
    def maxScore(self, s: str) -> int:
        from collections import Counter
        ans = []
        for i in range(1,len(s)):
            l = Counter(s[:i])
            r = Counter(s[i:])
            ans.append(Counter(l)['0'] + Counter(r)['1'])
            
        return max(ans)
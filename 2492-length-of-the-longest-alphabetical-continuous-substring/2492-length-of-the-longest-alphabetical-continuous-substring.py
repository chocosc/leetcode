class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        cur_max = 1
        ord_s = []
        for word in s:
            ord_s.append(ord(word))
        
        if len(s) == 1:
            return ans
        
        for i in range(1, len(ord_s)):
            if ord_s[i] - ord_s[i-1] == 1:
                ans += 1
                if ans > cur_max:
                    cur_max = ans
            else:
                ans = 1

        return cur_max
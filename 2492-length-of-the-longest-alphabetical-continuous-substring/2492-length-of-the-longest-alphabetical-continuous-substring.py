class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        cur_len = 1
        cur_max = 1
        
        ord_s = []
        for word in s:
            ord_s.append(ord(word))
        
        if len(s) == 1:
            return cur_max
        
        for i in range(1, len(ord_s)):
            if ord_s[i] - ord_s[i-1] == 1:
                cur_len += 1
                if cur_len > cur_max:
                    cur_max = cur_len
            else:
                cur_len = 1

        return cur_max
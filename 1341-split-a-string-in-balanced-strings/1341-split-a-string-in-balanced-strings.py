class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_sum = 0
        r_sum = 0
        ans = 0
        for i in s:
            if i == 'L':
                l_sum += 1
            elif i == 'R':
                r_sum += 1
            if l_sum == r_sum:
                ans += 1
                l_sum = 0
                r_sum = 0
        return ans
class Solution:
    def countDigits(self, num: int) -> int:
        from collections import Counter
        counter = Counter(str(num))
        ans = 0
        
        for key, value in counter.items():
            if num % int(key) == 0:
                ans += value

        return ans

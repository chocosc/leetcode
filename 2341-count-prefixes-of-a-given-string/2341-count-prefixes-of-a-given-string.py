class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefix = []
        ans = 0
        for i in range(len(s)):
            prefix.append(s[:i+1])
        for word in words:
            if word in prefix:
                ans += 1
        return ans
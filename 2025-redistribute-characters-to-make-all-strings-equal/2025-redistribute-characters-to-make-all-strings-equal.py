class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter()
        for word in words:
            c += Counter(word)
        for value in c.values():
            if value % len(words) != 0:
                return False
        return True
        




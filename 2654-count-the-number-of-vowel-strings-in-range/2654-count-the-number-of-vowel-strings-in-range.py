class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel_characters = 'aeiou'
        ans = 0
        for i in range(left, right+1):
            if words[i][0] in vowel_characters and words[i][-1] in vowel_characters:
                ans += 1
        return ans
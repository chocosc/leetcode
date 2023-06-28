class Solution:
    def getLucky(self, s: str, k: int) -> int:
        word_str = ''
        for word in s:
            word_str += str(ord(word)-96)
        for i in range(k):
            temp = 0
            for num in word_str:
                temp += int(num)
            word_str = str(temp)
        return int(word_str)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            gifts[gifts.index(max(gifts))] = int(gifts[gifts.index(max(gifts))] ** 0.5)
        return sum(gifts)
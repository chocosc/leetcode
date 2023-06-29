class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 1안
        # for _ in range(k):
        #     gifts[gifts.index(max(gifts))] = int(gifts[gifts.index(max(gifts))] ** 0.5)
        # return sum(gifts)

        for _ in range(k):
            gifts = sorted(gifts)
            gifts[-1] = int(gifts[-1] ** 0.5)
        
        return sum(gifts)
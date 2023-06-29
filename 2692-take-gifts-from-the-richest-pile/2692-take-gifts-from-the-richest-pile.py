class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 1안
        # for _ in range(k):
        #     gifts[gifts.index(max(gifts))] = int(gifts[gifts.index(max(gifts))] ** 0.5)
        # return sum(gifts)

        import math
        i = 0
        while i < k:
            gifts = sorted(gifts)
            sqrt = math.floor(math.sqrt(gifts[-1]))
            gifts[-1] = sqrt
            i +=1
        return sum(gifts)
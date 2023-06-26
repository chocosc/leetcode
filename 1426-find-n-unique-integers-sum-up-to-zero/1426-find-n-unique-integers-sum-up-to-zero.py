class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            nums1 = [-x-1 for x in range(n//2)]
            nums2 = [x+1 for x in range(n//2)]
            return nums1 + nums2
        else:
            nums1 = [-x for x in range(n//2+1)]
            nums2 = [x for x in range(1, n//2+1)]
            return nums1 + nums2

            
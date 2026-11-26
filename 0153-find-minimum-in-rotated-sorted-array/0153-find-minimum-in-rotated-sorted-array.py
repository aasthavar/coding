class Solution:
    def findMin(self, a: list[int]) -> int:
        l, r = 0, len(a) - 1

        while l < r:
            m = l + (r - l) // 2

            if a[m] > a[r]:
                l = m + 1
            else:
                r = m

        return a[l]
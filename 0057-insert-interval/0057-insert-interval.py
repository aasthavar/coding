# Naive approach â Insert, sort, merge
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # Find insertion position using binary search
        l, r = 0, len(intervals)

        while l < r:
            mid = (l + r) // 2
            if intervals[mid][0] < newInterval[0]:
                l = mid + 1
            else:
                r = mid

        intervals.insert(l, newInterval)

        # Merge intervals
        result = []

        for curr in intervals:
            if result and result[-1][1] >= curr[0]:
                result[-1][1] = max(result[-1][1], curr[1])
            else:
                result.append(curr)

        return result
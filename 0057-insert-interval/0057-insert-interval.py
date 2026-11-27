# Naive approach â search, insert, merge - O(logn + n + n) - O(n)
# class Solution:
#     def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
#         # Find insertion position using binary search
#         l, r = 0, len(intervals)

#         while l < r:
#             mid = (l + r) // 2
#             if intervals[mid][0] < newInterval[0]:
#                 l = mid + 1
#             else:
#                 r = mid

#         intervals.insert(l, newInterval)

#         # Merge intervals
#         result = []

#         for curr in intervals:
#             if result and result[-1][1] >= curr[0]:
#                 result[-1][1] = max(result[-1][1], curr[1])
#             else:
#                 result.append(curr)

#         return result

# Single pass: O(n)
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)

        # 1. Add intervals strictly before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # 3. Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
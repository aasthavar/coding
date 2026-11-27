class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort based on end values
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = float("-inf")

        for start, end in intervals:
            # this is the non-overlapping case
            if start >= prev_end:
                prev_end = end
            else:
                removals += 1

        return removals
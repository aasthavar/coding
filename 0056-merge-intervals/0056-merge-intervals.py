class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        st = [intervals[0]]
        for curr in intervals[1:]:
            if st[-1][1] >= curr[0]:
                st[-1][1] = max(st[-1][1], curr[1])
            else:
                st.append(curr)

        return st

    # def is_overlapping(self, a, b):
    #     # note: works only for sorted a, b
    #     if b[0] <= a[1]:
    #         return True
    #     return False
    # def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    #     intervals.sort(key=lambda x: x[0])
    #     n = len(intervals)
    #     st = [intervals[0]]
    #     i = 1
    #     while i<n:
    #         # print("initial", i, st)
    #         if st and self.is_overlapping(st[-1], intervals[i]):
    #             top = st[-1]
    #             st.pop()
    #             if intervals[i][1] >= top[1]: 
    #                 item = [top[0], intervals[i][1]]
    #             else:
    #                 item = [top[0], top[1]]
    #             st.append(item)
    #         else:
    #             st.append(intervals[i])
    #         # print("later", i, st)
    #         i += 1
    #     return st
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        nge_index = [0] * n
        st = []
        i = n - 1
        while i >= 0:
            while st and st[-1][0] <= temperatures[i]:
                st.pop()
            nge_index[i] = st[-1][1] if st else 0
            st.append((temperatures[i], i))
            i -= 1
        return [nge_index[i] - i if nge_index[i]!=0 else 0 for i in range(n)]
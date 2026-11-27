class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []

        for curr in asteroids:
            alive = True

            while st and curr < 0 and st[-1] > 0:
                if st[-1] < abs(curr):
                    st.pop()

                elif st[-1] == abs(curr):
                    st.pop()
                    alive = False
                    break

                else:
                    alive = False
                    break

            if alive:
                st.append(curr)

        return st
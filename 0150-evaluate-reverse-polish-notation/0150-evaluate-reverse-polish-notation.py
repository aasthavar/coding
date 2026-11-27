class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []

        for token in tokens:
            if token.lstrip('-').isdigit():
                st.append(int(token))
            else:
                b = st.pop()
                a = st.pop()

                if token == "+":
                    st.append(a + b)
                elif token == "-":
                    st.append(a - b)
                elif token == "*":
                    st.append(a * b)
                else:
                    st.append(int(a / b))

        return st[-1]
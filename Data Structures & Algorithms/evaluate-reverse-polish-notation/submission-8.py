class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_list = []
        if not tokens:
            return 0
        operators = {"+", "-", "*", "/"}
        for i, val in enumerate(tokens):
            if val not in operators:
                math_list.append(int(val))
            elif val in operators:
                b = math_list.pop()
                a = math_list.pop()
                if val == "+":
                    math_list.append(a+b)
                elif val == "-":
                    math_list.append(a-b)
                elif val == '/':
                    math_list.append(int(a/b))
                else:
                    math_list.append(a*b)
        return math_list[0]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_map = {')':'(', '}':'{', ']':'['}
        
        for char in s:
            if char not in valid_map:
                stack.append(char)
            else:
                if not stack or valid_map[char] != stack[-1]:
                    return False
                stack.pop()
        return not stack
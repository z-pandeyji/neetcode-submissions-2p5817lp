class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[ch] != top:
                    return False
        return len(stack) == 0
        
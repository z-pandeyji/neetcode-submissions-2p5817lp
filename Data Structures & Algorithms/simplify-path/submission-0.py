class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        i = 0
        while i < n:
            if path[i] == '/':
                i += 1
                continue
            temp = ""
            while i < n and path[i] != '/':
                temp += path[i]
                i += 1
            if temp == ".":
                continue
            elif temp == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(temp)
        if len(stack) == 0:
            return '/'
        result = ""
        for d in stack:
            result += "/" + d
            
        return result

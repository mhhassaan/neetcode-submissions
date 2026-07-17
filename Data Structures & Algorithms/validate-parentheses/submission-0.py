class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close2open = {")":"(", "]":"[", "}":"{"}

        for n in s:
            if n in close2open:
                if stack and stack[-1] == close2open[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)


        return True if not stack else False
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {'}':'{',')':'(',']':'['}
        for i in s:
            if i in close_open:
                if stack and stack[-1] == close_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
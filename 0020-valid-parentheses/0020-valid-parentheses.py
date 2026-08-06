class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in l:
                if not stack or stack.pop() != l[i]:
                    return False
            else:
                stack.append(i)
        return stack == []
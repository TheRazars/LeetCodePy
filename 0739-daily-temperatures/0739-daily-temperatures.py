class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and n > temperatures[stack[-1]]:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans
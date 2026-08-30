class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                cur_i = stack.pop()
                ans[cur_i] = i - cur_i
            stack.append(i)
        return ans
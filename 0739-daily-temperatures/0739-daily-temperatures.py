class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                cur_ind = stack.pop()
                ans[cur_ind] = i - cur_ind
            stack.append(i)
        return ans
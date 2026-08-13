class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        memory = []
        ans = [0] * len(temperatures)
        for i, curr in enumerate(temperatures):
            while memory and curr > temperatures[memory[-1]]:
                prev = memory.pop()
                ans[prev] = i - prev
            memory.append(i)
        return ans
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        best, left = 0, 0
        stack = []
        for right, n in enumerate(heights):
            while stack and n < heights[stack[-1]]:
                cur = stack.pop()
                left = stack[-1] + 1 if stack else 0
                w = right - left
                best = max(best, heights[cur] * w)
            stack.append(right)
        return best
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        best = 0
        for i, n in enumerate(heights):
            while stack and n < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                w = i - left - 1
                print(h, w)
                best = max(best, w*h)
            stack.append(i)    
        return best
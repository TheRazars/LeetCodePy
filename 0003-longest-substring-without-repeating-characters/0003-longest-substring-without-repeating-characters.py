class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        max_len = 0
        for right, i in enumerate(s):
            if i in last and last[i] >= left:
                left = last[i] + 1
            last[i] = right
            max_len = max(max_len, right - left + 1)
        return max_len
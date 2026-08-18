class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        left = 0
        max_c = 0
        max_len = 0
        for right, i in enumerate(s):
            c[i] = c.get(i, 0) + 1
            max_c = max(max_c, c[i])
            window = right - left + 1
            if window - max_c > k:
                c[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
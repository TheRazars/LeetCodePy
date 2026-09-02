class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_c = 0
        ans = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_c = max(max_c, count[s[right]])
            wdw = right - left + 1
            if wdw - max_c > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        for i in strs[1:]:
            n = 0

            while n < len(first) and n < len(i) and first[n] == i[n]:
                n += 1
            first = first[:n]
        return first
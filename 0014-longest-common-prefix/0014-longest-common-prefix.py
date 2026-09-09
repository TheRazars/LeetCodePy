class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        frst = strs[0]
        for i in strs[1:]:
            n = 0
            while n < len(frst) and n < len(i) and frst[n] == i[n]:
                n += 1
            frst = frst[:n]
        return frst
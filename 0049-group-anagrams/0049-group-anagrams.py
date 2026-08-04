class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dir = {}
        for i in strs:
            if "".join(sorted(i)) not in dir:
                dir["".join(sorted(i))] = []
            dir["".join(sorted(i))].append(i)
        return list(dir.values())
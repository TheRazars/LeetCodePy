class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dir = {}
        for i in strs:
            key = "".join(sorted(i))
            if "".join(sorted(i)) not in dir:
                dir[key] = []
            dir[key].append(i)
        return list(dir.values())
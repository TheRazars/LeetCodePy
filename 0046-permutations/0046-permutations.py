class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        r, s = [], []

        def backtracking(i):
            if i == n:
                r.append(s[:])
                return
            for x in nums:
                if x not in s:
                    s.append(x)
                    backtracking(i+1)
                    s.pop()
        backtracking(0)
        return r
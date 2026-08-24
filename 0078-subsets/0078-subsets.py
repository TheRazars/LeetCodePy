class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        r, s = [], []

        def backtracking(i):
            if i == n:
                r.append(s[:])
                return
            
            backtracking(i + 1)

            s.append(nums[i])
            backtracking(i + 1)
            s.pop()
        
        backtracking(0)
        return r
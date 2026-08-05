class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dir = {}
        for i, n in enumerate(numbers):
            w = target - n
            if w in dir:
                return (dir[w]+1, i+1)
            dir[n] = i
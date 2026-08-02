class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for i, n in enumerate(nums):
            num = target - n
            if num in memory:
                return [memory[num], i]
            memory[n] = i
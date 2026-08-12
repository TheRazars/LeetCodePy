class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            midd = (left + right) // 2
            if nums[midd] > nums[right]:
                left = midd + 1
            else:
                right = midd
        return nums[left]
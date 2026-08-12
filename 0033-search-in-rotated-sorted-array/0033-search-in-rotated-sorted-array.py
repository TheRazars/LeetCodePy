class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            midd = (left + right) // 2
            if nums[midd] == target:
                return midd
            
            if nums[left] <= nums[midd]:
                if nums[left] <= target < nums[midd]:
                    right = midd - 1
                else: 
                    left = midd + 1
            else:
                if nums[midd] < target <= nums[right]:
                    left = midd + 1
                else:
                    right = midd - 1
        return -1
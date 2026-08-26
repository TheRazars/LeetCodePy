class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        for i in numbers:
            s = numbers[left] + numbers[right]
            if s == target:
                return left + 1, right + 1
            elif s > target:
                right -= 1
            else:
                left += 1
            print(left, right)
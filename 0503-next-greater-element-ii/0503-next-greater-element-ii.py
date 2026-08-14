class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [-1] *  l
        memory = []
        for i in range(2 * l):
            num = nums[i % l]
            while memory and nums[memory[-1]] < num:
                prev = memory.pop()
                ans[prev] = num
                print("ttest")
            if i < l:
                memory.append(i)
        return ans
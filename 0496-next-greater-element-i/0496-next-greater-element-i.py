class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        mas = {}
        memory = []
        for i, n in enumerate(nums2):
            while memory and memory[-1] < n:
                prev = memory.pop()
                mas[prev] = n
            memory.append(n)
        for num in memory:
            mas[num] = -1
        for i in nums1:
            ans.append(mas[i])
        return ans

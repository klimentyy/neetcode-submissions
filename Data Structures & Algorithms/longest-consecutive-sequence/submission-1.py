class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        longest = 0
        p = 0

        while p < len(nums):
            start = p
            while p < (len(nums) - 1) and nums[p + 1] == nums[p] + 1:
                p += 1

            longest = max(longest, p - start + 1)
            p += 1

        return longest

        
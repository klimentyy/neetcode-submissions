class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = 0
        for i in range(len(nums)):
            c = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == c:
                    return [i, j]
        return []

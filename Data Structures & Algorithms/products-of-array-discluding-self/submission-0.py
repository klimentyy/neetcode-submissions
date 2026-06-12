class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        output = []

        for i in range(1, len(nums)):
            prefixes[i] = nums[i-1] * prefixes[i-1]
            
        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] = nums[i+1] * suffixes[i+1]

        for i in range(len(nums)):
            output.append(prefixes[i] * suffixes[i])
        
        return output
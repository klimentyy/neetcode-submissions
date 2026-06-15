class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums) - 2):
            target = - nums[i]
            r = len(nums) - 1
            l = i + 1

            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    continue
                if nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(res)




        


        
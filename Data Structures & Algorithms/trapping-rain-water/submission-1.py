class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        prefixes = []
        current_max = 0
        for h in height:
            current_max = max(current_max, h)
            prefixes.append(current_max)

        current_max = 0
        suffixes = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            current_max = max(current_max, height[i])
            suffixes[i] = current_max

        for i in range(len(height)):
            res += min(suffixes[i], prefixes[i]) - height[i]

        return res

            
            
            




        
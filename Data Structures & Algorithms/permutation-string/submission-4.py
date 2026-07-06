from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        origin_map = Counter(s1)
        window_map = Counter()
        l = 0
        r = 0
        for r in range(len(s1)):
            window_map[s2[r]] += 1
        
        if origin_map == window_map: return True

        while r < len(s2) - 1:
            r += 1
            window_map[s2[r]] += 1

            window_map[s2[l]] -= 1
            if window_map[s2[l]] == 0:
                window_map.pop(s2[l])
            l += 1

            if origin_map == window_map: return True

        return False

        


        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        char_map = [0] * 26

        for c in s1:
            char_map[a_ord(c)] += 1
        
        sliding_map = [0] * 26

        for i in range(len(s1)):
            sliding_map[a_ord(s2[i])] += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if sliding_map == char_map:
                return True
            sliding_map[a_ord(s2[r])] += 1
            sliding_map[a_ord(s2[l])] -= 1
            l += 1      
        return sliding_map == char_map
          

def a_ord(char: str):
    return ord(char) - ord('a')
        
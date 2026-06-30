class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        max_len = 0
        unq_ch = set()
        while r < len(s):
            while r < len(s) and s[r] not in unq_ch:
                unq_ch.add(s[r])
                r += 1
            max_len = max(max_len, r - l)
            unq_ch.remove(s[l]) 
            l += 1
        return max_len
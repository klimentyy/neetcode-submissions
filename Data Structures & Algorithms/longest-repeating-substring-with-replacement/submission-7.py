from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        r = 0
        counter = Counter()
        longest = 0
        replaced = 0

        for l in range(len(s)):
            if r >= len(s):
                break
            
            while r < len(s):
                counter[s[r]] += 1
                replaced = r - l + 1 - counter.most_common()[0][1]
                if replaced > k:
                    counter[s[r]] -= 1
                    break
                r += 1
            
            longest = max(longest, r - l)
            counter[s[l]] -= 1
            
        return longest
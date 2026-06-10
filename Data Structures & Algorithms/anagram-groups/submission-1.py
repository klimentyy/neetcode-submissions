class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = {}

        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            anagram_map.setdefault(tuple(count), []).append(w)
        
        return list(anagram_map.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = {}

        for w in strs:
            w_sort = "".join(sorted(w))
            anagram_map.setdefault(w_sort, []).append(w)
        
        return list(anagram_map.values())
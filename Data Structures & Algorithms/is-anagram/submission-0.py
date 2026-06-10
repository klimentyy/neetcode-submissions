class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}

        if len(s) != len(t):
            return False
        
        for c_s, c_t in zip(s, t):
            s_d[c_s] = s_d.get(c_s, 0) + 1
            t_d[c_t] = t_d.get(c_t, 0) + 1
        
        return s_d == t_d

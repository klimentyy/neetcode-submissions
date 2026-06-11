class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        d = '#'
        res = []
        p = 0

        while p < len(s):
            c = ''
            while s[p] != d:
                c += s[p]
                p += 1
            end =  p + int(c) + 1
            w = ''
            for i in range(p + 1, end):
                w += s[i]
            res.append(w)
            p = end
        return res


        

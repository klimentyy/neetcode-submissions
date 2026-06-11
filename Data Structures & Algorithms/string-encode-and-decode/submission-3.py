class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        p = 0

        while p < len(s):
            start = p
            while s[p] != '#':
                p += 1
            lenght = int(s[start:p])

            end = p + lenght + 1
            res.append(str(s[p+1:end]))
            p = end
        return res


        

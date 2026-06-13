class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        r_map = [set() for _ in range(n)]
        c_map = [set() for _ in range(n)]
        s_map = [set() for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                num = board[r][c]
                if num == '.':
                    continue
                if num in r_map[r]:
                    return False
                r_map[r].add(num)
                if num in c_map[c]:
                    return False
                c_map[c].add(num)
                s = (r // 3) * 3 + (c // 3)
                if num in s_map[s]:
                    return False
                s_map[s].add(num)

        return True


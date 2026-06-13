class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        r_map = [0] * 9
        c_map = [0] * 9
        s_map = [0] * 9
        
        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val == '.':
                    continue
                
                val = int(val) - 1
                num = 1 << val

                s = (r // 3) * 3 + (c // 3)

                if num & r_map[r]: return False
                if num & c_map[c]: return False
                if num & s_map[s]: return False
                
                r_map[r] |= num
                c_map[c] |= num     
                s_map[s] |= num

        return True


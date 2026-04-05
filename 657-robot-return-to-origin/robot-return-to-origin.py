class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for move in moves:
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            else:
                y -= 1
        if x == 0 and y == 0:
            return True
        return False
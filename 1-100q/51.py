class Solution:
    def solveNQueens(self, n: int):
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
    
    def search(self, state, solutions, n):
        if len(state) == n: # one more solution found
            sol_str = self.to_string(state, n)
            solutions.append(sol_str)
            return
        
        for candidate in self.possible_candidates(state, n):
            # recursion
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
    
    def possible_candidates(self, state, n):
        if not state:
            return range(n)
        
        position = len(state)
        candidates = set(range(n))
        
        for row, col in enumerate(state):
            # check row and col
            candidates.discard(col)
            # check diagonal
            diagonal = position - row
            
            candidates.discard(col + diagonal)
            candidates.discard(col - diagonal)
        
        return candidates
    
    def to_string(self, state, n):
        # [1, 3, 0, 2] -> [".Q..", "...Q", "Q...", "..Q."]
        result = []
        
        for i in state:
            result.append("." * i + "Q" + "." * (n - i - 1))
        
        return result
            
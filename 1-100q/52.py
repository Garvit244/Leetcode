class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = []
        state = []
        self.search(solutions, state, n)
        return len(solutions)
    
    def search(self, solutions, state, n):
        if len(state) == n:
            solutions.append(state)
            return
        
        for candidate in self.possible_candidates(state, n):
            state.append(candidate)
            self.search(solutions, state, n)
            state.pop()
    
    def possible_candidates(self, state, n):
        if not state:
            return range(n)
        
        position = len(state)
        candidates = set(range(n))
        
        for row, col in enumerate(state):
            # check row and col
            candidates.discard(col)
            
            #check diaconal
            dist = position - row
            candidates.discard(col - dist)
            candidates.discard(col + dist)
        
        return candidates
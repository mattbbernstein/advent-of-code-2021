class BingoBoard:

    def __init__(self, lines: list[list[int]]):
        '''Creates a bingo board from a list of rows'''
        assert len(lines) == 5
        
        self.board = []
        self.marked = []
        self.create_boards()
        
        rows = []
        for line in lines:
            line = line.strip()
            int_line = list(map(int, line.split()))
            assert len(int_line) == 5
            rows.append(int_line)

        self.board = rows
    
    def find(self, x: int) -> tuple[int, int]:
        '''Finds the number in board'''
        for r, row in enumerate(self.board):
            try:
                c = row.index(x)
                return (r, c)
            except ValueError:
                pass
        return (-1, -1)

    def mark(self, x: int) -> bool:
        '''Marks the input number and returns true if bingo'''
        r, c = self.find(x)
        if r >= 0 and c >= 0:
            self.marked[r][c] = True
        return self.check_board()

    def check_board(self) -> bool:
        '''Returns true if bingo'''
        for row in self.marked:
            if all(row):
                return True 

        for i in range(len(self.marked[0])):
            vert = [x[i] for x in self.marked]
            if all(vert):
                return True
        
        return False

    def score(self, x: int) -> int:
        '''Returns of the score of the board'''
        unmarked_sum = 0
        for r, row in enumerate(self.board):
            for c, val in enumerate(row):
                if not self.marked[r][c]:
                    unmarked_sum += val
        return unmarked_sum * x

    def __repr__(self):
        out = ''
        for r, row in enumerate(self.board):
            for c, val in enumerate(row):
                if self.marked[r][c]:
                    out += 'x\t'
                else:
                    out += str(val) + '\t'
            out += '\n'
        return out.strip()

    def create_boards(self):
        '''Create an empty 5x5 board filled with x'''
        for r in range(5):
            self.board.append([])
            self.marked.append([])
            for c in range(5):
                self.board[r].append(0)
                self.marked[r].append(False)
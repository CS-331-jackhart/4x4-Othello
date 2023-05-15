class Player:
    """Base player class"""
    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol
    
    def get_move(self, board):
        raise NotImplementedError()



class HumanPlayer(Player):
    """Human subclass with text input in command line"""
    def __init__(self, symbol):
        Player.__init__(self, symbol)
        self.total_nodes_seen = 0

    def clone(self):
        return HumanPlayer(self.symbol)
        
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return  (col, row)


class AlphaBetaPlayer(Player):
    """Class for Alphabeta AI: implement functions minimax, eval_board, get_successors, get_move
    eval_type: int
        0 for H0, 1 for H1, 2 for H2
    prune: bool
        1 for alpha-beta, 0 otherwise
    max_depth: one move makes the depth of a position to 1, search should not exceed depth
    total_nodes_seen: used to keep track of the number of nodes the algorithm has seearched through
    symbol: X for player 1 and O for player 2
    """
    def __init__(self, symbol, eval_type, prune, max_depth):
        Player.__init__(self, symbol)
        self.eval_type = eval_type
        self.prune = prune
        self.max_depth = int(max_depth) 
        self.max_depth_seen = 0
        self.total_nodes_seen = 0
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'


    def terminal_state(self, board):
        # If either player can make a move, it's not a terminal state
        for c in range(board.cols):
            for r in range(board.rows):
                if board.is_legal_move(c, r, "X") or board.is_legal_move(c, r, "O"):
                    return False 
        return True 


    def terminal_value(self, board):
        # Regardless of X or O, a win is float('inf')
        state = board.count_score(self.symbol) - board.count_score(self.oppSym)
        if state == 0:
            return 0
        elif state > 0:
            return float('inf')
        else:
            return -float('inf')


    def flip_symbol(self, symbol):
        # Short function to flip a symbol
        if symbol == "X":
            return "O"
        else:
            return "X"


    def alphabeta(self, board) -> (int, int):
        col, row = 0, 0

        val = -float('inf')

        for state in self.get_successors(board, self.symbol):
            newVal = self.min_value(state)
            if val < newVal:
                val = newVal
                col = state.move[0]
                row = state.move[1]

        if val == -float('inf'):
            newState = self.get_successors(board, self.symbol)[0]
            col = state.move[0]
            row = state.move[1]

        return col, row

    def max_value(self, board, alpha=-float('inf'), beta=float('inf'), depth=0) -> float:

        self.total_nodes_seen += 1

        # If we've reached a terminal state or max depth
        if self.terminal_state(board):
            return self.terminal_value(board)
        elif depth == self.max_depth:
            return self.eval_board(board)

        val = -float('inf')

        # Recursively find the best value out of all the successors
        for state in self.get_successors(board, self.symbol):
            val = max(val, self.min_value(state, alpha, beta, depth+1))

            if self.prune and val >= beta:
                return val
            alpha = max(alpha, val)


        return val

    def min_value(self, board, alpha=-float('inf'), beta=float('inf'), depth=0) -> float:

        self.total_nodes_seen += 1

        # If we've reached a terminal state or max depth
        if self.terminal_state(board):
            return self.terminal_value(board)
        elif depth == self.max_depth:
            return self.eval_board(board)

        val = float('inf')

        # Recursively find the worst value out of all the successors
        for state in self.get_successors(board, self.oppSym):
            val = min(val, self.max_value(state, alpha, beta, depth+1))

            if self.prune and val <= alpha:
                return val
            beta = min(beta, val)

        return val


    def eval_board(self, board) -> float:
        value = 0
        if self.eval_type == '0':
            value = board.count_score(self.symbol) - board.count_score(self.oppSym)
        elif self.eval_type == '1':
            value = len(self.get_successors(board, self.symbol)) - len(self.get_successors(board, self.oppSym))
        elif self.eval_type == '2':
            value = board.count_score(self.symbol)
        return value


    def get_successors(self, board, player_symbol) -> list:
        successors = []

        if not board.has_legal_moves_remaining(player_symbol):
            return []

        for x in range(board.cols):
            for y in range(board.rows):
                if board.has_legal_moves_remaining(player_symbol):
                    if board.is_legal_move(x, y, player_symbol):
                        #print(x, y)
                        newBoard = board.cloneOBoard()
                        newBoard.play_move(x, y, player_symbol)
                        newBoard.move = (x, y)
                        successors.append(newBoard)
                else:
                    return successors

        return successors 


    def get_move(self, board):
        # Write function that returns a move (column, row) here using minimax
        # type:(board) -> (int, int)
        return self.alphabeta(board)

       
        






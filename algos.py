"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x=count_o=0
    for row in board:
        count_x += row.count("X")
        count_o += row.count("O")
    if (count_o==count_x): return "X"
    else: return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==EMPTY:
                action.add((i,j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy
    if action is None or action[0]<0 or 2<action[0] or action[1]<0 or 2<action[1]\
         or board[action[0]][action[1]] != EMPTY: raise Exception
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]]= player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return(1 if winner(board)=="X" else -1 if winner(board)=="O"else 0)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # Check for immediate winning move for the current player
    current_player = player(board)
    for action in actions(board):
        new_board = result(board, action)
        if winner(new_board) == current_player:
            return action

    # Proceed with minimax if no immediate win found
    if current_player == X:
        return eval_max_mv(board)[1]
    else:
        return eval_min_mv(board)[1]

def eval_max_mv(board): #returning util/mv tuple
    if(terminal(board)): return utility(board), None

    cur_max_util = float('-inf')
    mv = None
    for a in actions(board):
        a_util, a_mv = eval_min_mv(result(board,a))
        if a_util>cur_max_util:
            cur_max_util, mv = a_util, a
            if cur_max_util == 1:
                return cur_max_util, mv
    return cur_max_util, mv
            
def eval_min_mv(board): #returning util/mv tuple
    if(terminal(board)): return utility(board),None
    cur_min_util = float('inf')
    mv = None
    for a in actions(board):
        a_util, a_mv = eval_max_mv(result(board,a))
        if a_util<cur_min_util:
            cur_min_util, mv = a_util, a
            if cur_min_util == -1:
                return cur_min_util, mv
    return cur_min_util, mv

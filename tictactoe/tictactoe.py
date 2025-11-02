"""
Tic Tac Toe Player
"""

import math
import copy

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
    # if terminal board return
    if terminal(board) is not False:
        return "Game Over!"

    # if board is empty, x starts
    if board == [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]:
        return X

    # track amount of xs and os played 
    xs = 0
    os = 0
    for row in board:
        for box in row:
            if box == X:
                xs += 1
            elif box == O:
                os += 1
    if xs > os:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # if terminal board return
    if terminal(board) is not False:
        return "Game Over!"
    
    empty_boxes = set()
    for i, row in enumerate(board):
        for j, box in enumerate(row):
            if box == EMPTY:
                empty_boxes.add((i, j))
    
    return empty_boxes


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    column = action[1]
    # learned how to check if a number is negative from:
    # https://pieriantraining.com/how-to-check-if-a-number-is-negative-in-python-a-beginners-guide/
    if 2 > row < 0 or 2 > column < 0:
        raise Exception
    if board[row][column] == EMPTY:
        board_copy = copy.deepcopy(board)
        board_copy[row][column] = player(board)
        return board_copy
    else:
        raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check for horizontal winner
    for row in board:
        if X not in row and EMPTY not in row:
            return O
        elif O not in row and EMPTY not in row:
            return X
    
    # check for vertical winner
    for column in range(3):
        board_column = []
        for row in range(3):
            board_column.append(board[row][column])
        if X not in board_column and EMPTY not in board_column:
            return O
        elif O not in board_column and EMPTY not in board_column:
            return X
        
    # check for diagonal winner
    d_wins = [[[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
 
    for d in d_wins:
        board_diagonal = []
        for row, column in d:
            board_diagonal.append(board[row][column])
        if X not in board_diagonal and EMPTY not in board_diagonal:
            return O
        elif O not in board_diagonal and EMPTY not in board_diagonal:
            return X
    
    # if no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for [i, k, j] in board:
            # if a box is empty game isnt over
            if EMPTY in [i, k, j]:
                return False
        # if no box is empty game is over
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        # create a list of dicts with all the possible actions and the min-value of the board
        results = [{"action": a, "value": min_value(result(board, a))} for a in actions(board)]
        # get the action value pair with the max value
        max_result = max(results, key=lambda r: r["value"])
        # return the action of max_result
        return max_result.get("action")
        
    else:
        results = [{"action": a, "value": max_value(result(board, a))} for a in actions(board)]
        min_result = min(results, key=lambda r: r["value"])
        return min_result.get("action")


def max_value(board):
    # first check if game is over and if so return utility
    if terminal(board) is not False:
        return utility(board)
    # asign v to negative infinity to asign v to the first value
    v = -math.inf
    for action in actions(board):
        # pick the max of current value (v) or new value
        v = max([v, pruned_min_value(result(board, action), v)])
    return v


def min_value(board):
    if terminal(board) is not False:
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min([v, pruned_max_value(result(board, action), v)])
    return v


def pruned_max_value(board, current_value):
    # first check if game is over and if so return utility
    if terminal(board) is not False:
        return utility(board)
    # asign v to negative infinity to asign v to the first value
    v = -math.inf
    for action in actions(board):
        # pick the max of current value (v) or new value
        v = max([v, pruned_min_value(result(board, action), v)])
        if v >= current_value:
            return math.inf
    return v


def pruned_min_value(board, current_value):
    if terminal(board) is not False:
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min([v, pruned_max_value(result(board, action), v)])
        # if v is less than or equal to what max player already has, return -infinity
        # telling max player not to play this action
        if v <= current_value:
            return -math.inf
    return v
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

    if board == initial_state():
        return X

    if terminal(board):
        return None

    x = 0
    o = 0
    for row in board:
        for cell in row:
            if cell == X:
                x += 1
            elif cell == O:
                o += 1

    if x > o:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None

    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Not a valid action!")
    if action[0] not in range(3) or action[1] not in range(3):
        raise Exception("Out of bounds!")

    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if all(cell == X for cell in board[i]):
            return X
        if all(cell == O for cell in board[i]):
            return O
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O

    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for i in range(3):
        if any(cell == EMPTY for cell in board[i]):
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    status = winner(board)

    if status == X:
        return 1
    if status == O:
        return -1
    return 0


iteration = 1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global iteration
    if terminal(board):
        if iteration == 1:
            return None
        iteration -= 1
        return utility(board)

    current_player = player(board)
    results = []
    possible_actions = actions(board)
    optimal_result = []
    if possible_actions:
        for action in possible_actions:
            iteration += 1
            results.append(minimax(result(board, action)))
        if current_player == X:
            optimal_result = max(results)
        else:
            optimal_result = min(results)
        if iteration == 1:
            for action, current_result in zip(possible_actions, results):
                if current_result == optimal_result:
                    return action
    iteration -= 1
    return optimal_result

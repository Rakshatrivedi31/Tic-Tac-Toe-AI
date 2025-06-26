# ai.py
import math

def is_winner(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = "O"
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = "X"
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

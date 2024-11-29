board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':  
        return 10 - depth
    elif winner == 'O':  
        return depth - 10
    elif is_draw(board):  
        return 0

    if is_maximizing:  
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:  
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(best_score, score)
        return best_score


def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return 10 - depth
    elif winner == 'O':
        return depth - 10
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = ' '
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = ' '
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score



def best_move(board):
    best_score = float('-inf')
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        
        display_board(board)
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move!")
            continue

        if check_winner(board) == 'O':
            display_board(board)
            print("You win!")
            break
        elif is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'

        if check_winner(board) == 'X':
            display_board(board)
            print("AI wins!")
            break
        elif is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

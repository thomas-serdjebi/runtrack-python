class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = [['O' for _ in range(j)] for _ in range(i)]

    def play(self, column, color):
        if color != 'J' and color != 'R':
            print('Invalid color')
            return False

        if column < 0 or column >= self.j:
            print('Invalid column')
            return False

        i = self.i - 1
        while i >= 0 and self.board[i][column] != 'O':
            i -= 1

        if i < 0:
            print('Column is full')
            return False

        self.board[i][column] = color
        return True

    def print(self):
        for i in range(self.i):
            for j in range(self.j):
                print(self.board[i][j], end=' ')
            print()

def play_game():
    board = Board(6, 7)
    print('Welcome to the game of Connect Four!')
    board.print()
    player = 'J'

    while True:
        column = int(input(f'Player {player}, please choose a column to play (0 to {board.j-1}): '))
        if board.play(column, player):
            board.print()
            if check_winner(board, player):
                print(f'Player {player} wins!')
                print('Congratulations, you win 100 000 euros!')
                break
            player = 'R' if player == 'J' else 'J'

def check_winner(board, color):
    # Check horizontal
    for i in range(board.i):
        for j in range(board.j-3):
            if board.board[i][j] == color and board.board[i][j+1] == color and board.board[i][j+2] == color and board.board[i][j+3] == color:
                return True

    # Check vertical
    for i in range(board.i-3):
        for j in range(board.j):
            if board.board[i][j] == color and board.board[i+1][j] == color and board.board[i+2][j] == color and board.board[i+3][j] == color:
                return True

    # Check diagonal (top-left to bottom-right)
    for i in range(board.i-3):
        for j in range(board.j-3):
            if board.board[i][j] == color and board.board[i+1][j+1] == color and board.board[i+2][j+2] == color and board.board[i+3][j+3] == color:
                return True

    # Check diagonal (bottom-left to top-right)
    for i in range(3, board.i):
        for j in range(board.j-3):
            if board.board[i][j] == color and board.board[i-1][j+1] == color and board.board[i-2][j+2] == color and board.board[i-3][j+3] == color:
                return True

    return False

play_game()

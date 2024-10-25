class Piece:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, start, end, board):
        pass

    def get_symbol(self):
        pass


class King(Piece):
    def is_valid_move(self, start, end, board):
        # Kings can move one square in any direction
        return abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1

    def get_symbol(self):
        return 'K' if self.color == 'white' else 'k'


class Empty(Piece):
    def __init__(self):
        super().__init__(None)

    def is_valid_move(self, start, end, board):
        return False

    def get_symbol(self):
        return '.'


class Board:
    def __init__(self):
        self.board = [[Empty() for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Place Kings for demonstration, add other pieces as needed
        self.board[0][4] = King('black')  # Black King
        self.board[7][4] = King('white')  # White King
        # Other pieces setup here...

    def print_board(self):
        for row in self.board:
            print(" ".join(piece.get_symbol() for piece in row))

    def move_piece(self, start, end):
        sx, sy = start
        ex, ey = end
        piece = self.board[sx][sy]

        if isinstance(piece, Empty):
            return False  # No piece to move

        if piece.is_valid_move(start, end, self.board) and (isinstance(self.board[ex][ey], Empty) or self.board[ex][ey].color != piece.color):
            self.board[ex][ey] = piece
            self.board[sx][sy] = Empty()
            return True

        return False



class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'

    def make_move(self, start, end):
        piece = self.board.board[start[0]][start[1]]
        if piece.color != self.current_turn:
            print(f"It's {self.current_turn}'s turn!")
            return False

        if self.board.move_piece(start, end):
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            return True
        else:
            print("Invalid move!")
            return False

    def print_board(self):
        self.board.print_board()



def parse_move(move_str):
    """Parse a move in the form 'e2 e4' into start and end tuples."""
    cols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    try:
        start, end = move_str.split()
        start = (8 - int(start[1]), cols[start[0]])
        end = (8 - int(end[1]), cols[end[0]])
        return start, end
    except (ValueError, KeyError):
        return None, None


def main():
    game = Game()

    while True:
        game.print_board()
        move_str = input(f"{game.current_turn}'s move (e.g., 'e2 e4'): ")
        start, end = parse_move(move_str)

        if start is None or end is None:
            print("Invalid input format. Please use 'e2 e4' format.")
            continue

        if not game.make_move(start, end):
            print("Try again!")

if __name__ == "__main__":
    main()

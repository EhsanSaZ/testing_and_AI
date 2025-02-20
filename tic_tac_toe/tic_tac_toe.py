class Player:
    wins = 0

    def __init__(self, name="", piece=''):
        self.name = name
        self.piece = piece

    def __str__(self):
        return self.piece

    def won_game(self):
        self.wins += 1
        return self.name


class Board:
    dimensions = 3
    spaces = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    # def __init__(self, dimensions=3):
    #     self.dimensions = dimensions
    #     TODO: dynamically size the 2D array

    def __str__(self):
        board_string = ""
        for row in self.spaces:
            for space in row:
                board_string += space + ' '
            board_string += '\n'
        return board_string

    def clear(self):
        self.spaces = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def space_empty(self, row, col):
        if self.valid_move(row, col):
            return self.spaces[row - 1][col - 1] == ' '

        raise Exception("move is out of bounds")

    def valid_move(self, row, col):
        if row > self.dimensions or col > self.dimensions:
            return False

        if row < 1 or col < 1:
            return False

        return True

    def is_full(self):
        for row in self.spaces:
            for space in row:
                if space == ' ':
                    return False

        return True

    def is_empty(self):
        for row in self.spaces:
            for space in row:
                if space != ' ':
                    return False

        return True

    def in_a_row(self):
        return self.diagonal() or self.horizontal() or self.vertical()

    def diagonal(self):
        if self.is_empty():
            return 0

        if self.spaces[0][0] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[2][2]:
            return 1

        if self.spaces[2][0] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[0][2]:
            return 2

        return 0

    def horizontal(self):
        if self.is_empty():
            return 0

        if ' ' not in self.spaces[0] and self.spaces[0][0] == self.spaces[0][1] and self.spaces[0][1] == self.spaces[0][2]:
            return 1

        if ' ' not in self.spaces[1] and self.spaces[1][0] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[1][2]:
            return 2

        if ' ' not in self.spaces[2] and self.spaces[2][0] == self.spaces[2][1] and self.spaces[2][1] == self.spaces[2][2]:
            return 3

        return 0

    def vertical(self):
        if self.is_empty():
            return 0

        if self.spaces[0][0] != ' ' and self.spaces[0][0] == self.spaces[1][0] and self.spaces[1][0] == self.spaces[2][0]:
            return 1

        if self.spaces[0][1] != ' ' and self.spaces[0][1] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[2][1]:
            return 2

        if self.spaces[0][2] != ' ' and self.spaces[0][2] == self.spaces[1][2] and self.spaces[1][2] == self.spaces[2][2]:
            return 3

        return 0

    def update(self, row, col, piece):
        if self.space_empty(row, col):
            self.spaces[row - 1][col - 1] = piece

        return self.__str__()


class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.set_up()

    def set_up(self):
        self.board.clear()
        self.player1.piece = 'X'
        self.player2.piece = 'O'
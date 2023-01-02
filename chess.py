# Фигуры
# Пешка 1 Y+1 (взятие xy+1) (особое Y+2)
# Конь 2 (X+2Y+1)(X+2Y-1)(X-2Y+1)(X-2Y-1)(Y+2X+1)(Y+2X-1)(Y-2X+1)(Y-2X-1)
# Слон 3 xy+n xy-n x+y-n x-y+n
# Ладья 4 x+n y+n x-n y-n
# Ферзь 5 (xy+n xy-n x+y-n x-y+n) (x+n y+n x-n y-n)
# Король 6 x+-1 y+-1 xy+-1
pieces_start = [('p', 'w', 2, 1), ('p', 'w', 2, 2), ('p', 'w', 2, 3), ('p', 'w', 2, 4),
                ('p', 'w', 2, 5), ('p', 'w', 2,
                                   6), ('p', 'w', 2, 7), ('p', 'w', 2, 8),
                ('r', 'w', 1, 1), ('r', 'w', 1,
                                   8), ('k', 'w', 1, 2), ('k', 'w', 1, 7),
                ('b', 'w', 1, 3), ('b', 'w', 1,
                                   6), ('q', 'w', 1, 4), ('g', 'w', 1, 5),

                ('p', 'b', 7, 1), ('p', 'b', 7,
                                   2), ('p', 'b', 7, 3), ('p', 'b', 7, 4),
                ('p', 'b', 7, 5), ('p', 'b', 7,
                                   6), ('p', 'b', 7, 7), ('p', 'b', 7, 8),
                ('r', 'b', 8, 1), ('r', 'b', 8,
                                   8), ('k', 'b', 8, 2), ('k', 'b', 8, 7),
                ('b', 'b', 8, 3), ('b', 'b', 8, 6), ('q', 'b', 8, 4), ('g', 'b', 8, 5)]


pieces_start_dict = {}
for piece in pieces_start:
    cords = str(piece[2]) + str(piece[3])
    pieces_start_dict[cords] = piece[:2]


class Chess:
    def __init__(self, start_pieces):
        self.pieces = start_pieces
        self.current_player = 0
        self.black_king_state = 0  # 0 - ничего, 1 - шах
        self.white_king_state = 0

    def get_current_player(self):
        return self.current_player

    def get_piece_by_position(self, x, y):
        cords = str(x) + str(y)
        if cords in self.pieces:
            return (x, y, *self.pieces[cords])
        return 0

    def get_available_moves(self, piece):
        name, color, x, y = piece
        if name == 'p':
            if colour == 'w':
                if x == 2:
                    return (x+1, y), (x+2, y)
                return (x+1, y)
            if colour == 'b':
                if x == 7:
                    return (x-1, y), (x-2, y)
                return (x-1, y)

    def move(self, piece, x, y):
        name, colour, cx, cy = piece
        cords = str(cx) + str(cy)
        newcords = str(x) + str(y)
        if not cords in self.pieces:
            return 0
        if not (x, y) in self.get_available_moves(piece):
            return 1
        info = self.pieces[cords]
        self.pieces.pop(cords)
        self.pieces[newcords] = info

        self.current_player = not self.current_player
        return 2


chess = Chess(pieces_start_dict)
print(chess.get_piece_by_position(5, 7))
print(chess.get_available_moves(piece))
print(chess.get_current_player())
print(chess.move(1, 1, 1))
print(chess.get_current_player())

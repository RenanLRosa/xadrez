from classes.piece import Piece


class Pawn (Piece):
  def __init__(self, color, initial_position):
    self.image_file = './assets/' + color + 'Pawn.png'
    self.points = 1
    super().__init__(self.image_file, color, initial_position)

  def availablePositions(self, table):
    return_possibilities = []

    if (self.color == 'black'):
      for i in (-1, 1):
        new_position = (self.actualPosition()[0] + i, self.actualPosition()[1] + 1)
        other_piece = table.findPiece(new_position)
        if other_piece != None and other_piece.color != self.color:
          return_possibilities.append([new_position, other_piece])

      if (len(self.historic_positions) > 1):
        new_position = (self.actualPosition()[0], self.actualPosition()[1] + 1)
        other_piece = table.findPiece(new_position)
        if Piece.validPosition(new_position):
          if other_piece == None:
            return_possibilities.append([new_position, other_piece])
      else:
        for i in range(1, 3, 1):
          new_position = (self.actualPosition()[0], self.actualPosition()[1] + i)
          other_piece = table.findPiece(new_position)
          if Piece.validPosition(new_position):
            if other_piece == None:
              return_possibilities.append([new_position, other_piece])

    else:
      for i in (-1, 1):
        new_position = (self.actualPosition()[0] + i, self.actualPosition()[1] - 1)
        other_piece = table.findPiece(new_position)
        if other_piece != None and other_piece.color != self.color:
          return_possibilities.append([new_position, other_piece])

      if (len(self.historic_positions) > 1):
        new_position = (self.actualPosition()[0], self.actualPosition()[1] - 1)
        other_piece = table.findPiece(new_position)
        if Piece.validPosition(new_position) and other_piece == None:
          return_possibilities.append([new_position, other_piece])
      else:
        for i in range(1, 3, 1):
          new_position = (self.actualPosition()[0], self.actualPosition()[1] - i)
          other_piece = table.findPiece(new_position)
          if Piece.validPosition(new_position) and other_piece == None:
            return_possibilities.append([new_position, other_piece])

    return return_possibilities

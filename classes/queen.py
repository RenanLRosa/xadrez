from classes.piece import Piece


class Queen(Piece):
  def __init__(self, color, initial_position):
    self.image_file = './assets/' + color + 'Queen.png'
    super().__init__(self.image_file, color, initial_position)

  def availablePositions(self, table):
    move_positions = []
    atack_positions = []

    for sum_y in (-1, 0, 1):
      for sum_x in (-1, 0, 1):
        if sum_x == 0 and sum_y == 0:
          continue
        new_position = self.actualPosition()
        count = 0
        other_piece = None
        while Piece.validPosition(new_position) and other_piece == None:
          if count != 0:
            move_positions.append(new_position)
          count = count + 1
          new_position = (new_position[0] + sum_x, new_position[1] + sum_y)
          other_piece = table.findPiece(new_position)

        if other_piece != None and other_piece.color != self.color:
          atack_positions.append(new_position)

    return { 'move': move_positions, 'atack': atack_positions }

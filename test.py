
from classes.player import Player
from main import main


mocked_configuration = [
  ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
  ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn'],
  [],
  [],
  [None, 'white_pawn'],
  [],
  ['white_pawn', None, 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
  ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
]


players = [Player(False, 'white', 'IA 1'), Player(False, 'black', 'IA 2')]
main(players, initial_configuration=mocked_configuration)
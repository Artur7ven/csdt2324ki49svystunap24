import unittest
from unittest.mock import patch, MagicMock
from Game import Game
from Board import Board
from Pawn import Pawn
from King import King
from Tile import Tile
from Piece import Piece

class TestCheckers(unittest.TestCase):
    def setUp(self):
        pygame = MagicMock()
        pygame.init = MagicMock()

    def test_board_creation(self):
        board = Board(100, 100, 8)
        self.assertEqual(len(board.tile_list), 64)

    def test_pawn_creation(self):
        board = Board(100, 100, 8)
        pawn = Pawn(1, 2, 'black', board)
        self.assertEqual(pawn.color, 'black')
        self.assertEqual(pawn.x, 1)
        self.assertEqual(pawn.y, 2)
        self.assertFalse(pawn.has_moved)

    def test_king_creation(self):
        board = Board(100, 100, 8)
        king = King(3, 4, 'red', board)
        self.assertEqual(king.color, 'red')
        self.assertEqual(king.x, 3)
        self.assertEqual(king.y, 4)
        self.assertFalse(king.has_moved)

    def test_tile_creation(self):
        tile = Tile(2, 3, 50, 50)
        self.assertEqual(tile.color, 'dark')
        self.assertEqual(tile.coord, 'c4')
        self.assertIsNone(tile.occupying_piece)

    def test_piece_creation(self):
        board = Board(100, 100, 8)
        piece = Piece(5, 6, 'black', board)
        self.assertEqual(piece.color, 'black')
        self.assertEqual(piece.x, 5)
        self.assertEqual(piece.y, 6)

    def test_pawn_possible_moves(self):
        board = Board(100, 100, 8)
        pawn = Pawn(2, 3, 'black', board)
        moves = pawn._possible_moves()
        self.assertEqual(moves, [(-1, +1), (+1, +1)])

    def test_king_possible_moves(self):
        board = Board(100, 100, 8)
        king = King(4, 5, 'red', board)
        moves = king._possible_moves()
        self.assertEqual(moves, [(-1, -1), (+1, -1), (-1, +1), (+1, +1)])

    @patch('builtins.print')
    def test_game_message(self, mock_print):
        game = Game()
        game.winner = 'red'
        game.message()
        mock_print.assert_called_with('red Wins!!')

if __name__ == '__main__':
    unittest.main()
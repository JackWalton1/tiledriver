# Name:         Jack Walton
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Winter 2021

import unittest

import tiledriver
from tiledriver import PuzzleState as PS  # only allowed use of from ... import

class TestCreateGrid(unittest.TestCase):

    def test_create_grid_1(self):
        state = PS((3, 2, 1, 0), "")
        grid = [[3, 2], 
                [1, 0]]
        self.assertEqual(tiledriver.create_grid(state.tiles), grid)

    def test_create_grid_2(self):
        state = PS((3, 7, 1, 0, 4, 2, 6, 8, 5), "")
        grid = [[3, 7, 1],
                [0, 4, 2], 
                [6, 8, 5]]
        self.assertEqual(tiledriver.create_grid(state.tiles), grid)

    def test_create_grid_3(self):
        state = PS((3, 7, 1, 0, 4, 2, 6, 8, 5, 10, 11, 12, 13, 14, 15, 16), "")
        grid = [[3, 7, 1, 0],
                [4, 2, 6, 8],
                [5, 10, 11, 12],
                [13, 14, 15, 16]]
        self.assertEqual(tiledriver.create_grid(state.tiles), grid)

    def test_create_grid_4(self):
        state = PS((3, 7, 1, 0, 4), "")
        grid = [[3, 7],
                [1, 0],
                [4]]
        self.assertEqual(tiledriver.create_grid(state.tiles), grid)

    def test_create_grid_5(self):
        state = PS((3, 7, 1, 0, 4, 2, 6, 8, 5, 10), "")
        grid = [[3, 7, 1],
                [0, 4, 2], 
                [6, 8, 5], 
                [10]]
        self.assertEqual(tiledriver.create_grid(state.tiles), grid)

    def test_create_grid_6(self):
        state = PS((), "")
        grid = [[]]
        self.assertEqual(tiledriver.create_grid(state.tiles), grid)



class TestGetZeroIndex(unittest.TestCase):

    def test_get_zero_index_1(self):
        tiles = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(tiledriver.get_zero_index(tiles), 0)
    
    def test_get_zero_index_2(self):
        tiles = (4, 1, 2, 3, 0, 5, 6, 7, 8)
        self.assertEqual(tiledriver.get_zero_index(tiles), 4)

    def test_get_zero_index_3(self):
        tiles = (8, 1, 2, 3, 4, 5, 6, 7, 0)
        self.assertEqual(tiledriver.get_zero_index(tiles), 8)

    def test_get_zero_index_4(self):
        tiles = (1, 7, 2, 3, 4, 5, 6, 0, 8)
        self.assertEqual(tiledriver.get_zero_index(tiles), 7)

    def test_get_zero_index_5(self):
        tiles = (3, 1, 2, 0, 4, 5, 6, 7, 8)
        self.assertEqual(tiledriver.get_zero_index(tiles), 3)



class TestFindPosMoves(unittest.TestCase):

    def test_find_pos_moves_1(self):
        puzzle = tiledriver.create_grid((3, 2, 1, 0))
        self.assertEqual(tiledriver.find_pos_moves(puzzle, ""), ["J", "L"])

    def test_find_pos_moves_2(self):
        puzzle = tiledriver.create_grid((3, 0, 2, 1))
        self.assertEqual(tiledriver.find_pos_moves(puzzle, "J"), ["L"])

    def test_find_pos_moves_3(self):
        puzzle = tiledriver.create_grid((3, 7, 1, 4, 0, 2, 6, 8, 5))
        self.assertEqual(tiledriver.find_pos_moves(puzzle, "L"), \
            ["K", "J", "L"])

    def test_find_pos_moves_4(self):
        puzzle = tiledriver.create_grid((3, 7, 1, 0, 4, 2, 6, 8, 5))
        self.assertEqual(tiledriver.find_pos_moves(puzzle, ""), \
            ["K", "J", "H"])

    def test_find_pos_moves_5(self):
        puzzle = tiledriver.create_grid((3, 7, 1, 5, 4, 2, 6, 8, 0))
        self.assertEqual(tiledriver.find_pos_moves(puzzle, "L"), ["J", "L"])



class TestMakePuzzleMove(unittest.TestCase):

    def test_make_puzzle_move_1(self):
        tiles = (1, 2, 3, 6, 4, 5, 0, 7, 8)
        mtiles = (1, 2, 3, 0, 4, 5, 6, 7, 8)
        self.assertEqual(tiledriver.make_puzzle_move(tiles, "J"), mtiles)

    def test_make_puzzle_move_2(self):
        tiles = (5, 7, 0, 8)
        mtiles = (0, 7, 5, 8)
        self.assertEqual(tiledriver.make_puzzle_move(tiles, "J"), mtiles)

    def test_make_puzzle_move_3(self):
        tiles = (0, 7, 5, 8)
        mtiles = (5, 7, 0, 8)
        self.assertEqual(tiledriver.make_puzzle_move(tiles, "K"), mtiles)

    def test_make_puzzle_move_4(self):
        tiles = (1, 2, 0, 6, 4, 5, 3, 7, 8)
        mtiles = (1, 2, 5, 6, 4, 0, 3, 7, 8)
        self.assertEqual(tiledriver.make_puzzle_move(tiles, "K"), mtiles)

    def test_make_puzzle_move_5(self):
        tiles = (1, 2, 5, 6, 4, 8, 7, 0, 3)
        mtiles = (1, 2, 5, 6, 4, 8, 7, 3, 0)
        self.assertEqual(tiledriver.make_puzzle_move(tiles, "H"), mtiles)

    def test_make_puzzle_moves_6(self):
        tiles = (0, 8, 7, 3)
        mtiles = (8, 0, 7, 3)
        self.assertEqual(tiledriver.make_puzzle_move(tiles, "H"), mtiles)

    def test_make_puzzle_moves_7(self):
        tiles = (1, 2, 5, 6, 4, 8, 7, 3, 0)
        mtiles = (1, 2, 5, 6, 4, 8, 7, 0, 3)
        self.assertEqual(tiledriver.make_puzzle_move(tiles, "L"), mtiles)

    def test_make_puzzle_moves_8(self):
        tiles = (8, 0, 7, 3)
        mtiles = (0, 8, 7, 3)
        self.assertEqual(tiledriver.make_puzzle_move(tiles, "L"), mtiles)



class TestMakeAdjacent(unittest.TestCase):

    def test_make_adjacent_1(self):
        state = PS((3, 2, 1, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state), \
                         [PS((3, 0, 1, 2), "J"), PS((3, 2, 0, 1), "L")])

    def test_make_adjacent_2(self):
        state = PS((1, 2, 3, 0, 4, 5, 6, 7, 8), "")
        self.assertEqual(tiledriver.make_adjacent(state), \
                         [PS((1, 2, 3, 6, 4, 5, 0, 7, 8), "K"), \
                             PS((0, 2, 3, 1, 4, 5, 6, 7, 8), "J"), \
                                 PS((1, 2, 3, 4, 0, 5, 6, 7, 8), "H")])

    def test_make_adjacent_3(self):
        state = PS((1, 2, 3, 0, 4, 5, 6, 7, 8), "K") 
        self.assertEqual(tiledriver.make_adjacent(state), \
                         [PS((1, 2, 3, 6, 4, 5, 0, 7, 8), "KK"), \
                            PS((1, 2, 3, 4, 0, 5, 6, 7, 8), "KH")])

    def test_make_adjacent_4(self):
        state = PS((1, 2, 3, 0, 4, 5, 6, 7, 8), "L")
        self.assertEqual(tiledriver.make_adjacent(state), \
                         [PS((1, 2, 3, 6, 4, 5, 0, 7, 8), "LK"), \
                             PS((0, 2, 3, 1, 4, 5, 6, 7, 8), "LJ")])

    def test_make_adjacent_5(self):
        state = PS((1, 2, 3, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state), \
                          [PS((1, 0, 3, 2), "J"), PS((1, 2, 0, 3), "L")])

    def test_make_adjacent_6(self):
        state = PS((1, 0, 3, 2), "J")
        self.assertEqual(tiledriver.make_adjacent(state), \
                          [PS((0, 1, 3, 2), "JL")])



class TestFindInversions(unittest.TestCase):

    def test_find_inversions_1(self):
        self.assertEqual(tiledriver.find_inversions((3, 2, 1, 0)), 3)

    def test_find_inversions_2(self):
        self.assertEqual(tiledriver.find_inversions((0, 2, 1, 3)), 1)

    def test_find_inversions_3(self):
        tiles = (3, 7, 1, 4, 0, 2, 6, 8, 5)
        self.assertEqual(tiledriver.find_inversions(tiles), 10)

    def test_find_inversions_4(self):
        self.assertEqual(tiledriver.find_inversions((0, 1, 2, 3)), 0)

    def test_find_inversions_5(self):
        self.assertEqual(tiledriver.find_inversions((1, 0, 2, 3)), 0)



class TestIsSolvable(unittest.TestCase):

    def test_is_solvable_1(self):
        self.assertTrue(tiledriver.is_solvable((3, 2, 1, 0)))

    def test_is_solvable_2(self):
        self.assertFalse(tiledriver.is_solvable((0, 2, 1, 3)))

    def test_is_solvable_3(self):
        self.assertTrue(tiledriver.is_solvable((3, 7, 1, 4, 0, 2, 6, 8, 5)))

    def test_is_solvable_4(self):
        self.assertFalse(tiledriver.is_solvable((3, 7, 1, 2, 0, 4, 6, 8, 5)))

    def test_is_solvable_5(self):
        self.assertFalse(tiledriver.is_solvable((1, 2, 0, 3)))



class TestSolvePuzzle(unittest.TestCase):

    def test_solve_puzzle_1(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 2, 1, 0)), "JLKHJL")

    def test_solve_puzzle_2(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 7, 1, 4, 0, 2, 6, 8, \
            5)), "JHKKLJLJ")

    def test_solve_puzzle_3(self):
        self.assertEqual(tiledriver.solve_puzzle((1, 0, 2, 3)), "L")

    def test_solve_puzzle_4(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 2, 0, 1)), "JHKLJ")

    def test_solve_puzzle_5(self):
        self.assertEqual(tiledriver.solve_puzzle((1, 0, 2, 3, 4, 5, 6, 7, \
            8)), "L")


if __name__ == "__main__":
    unittest.main()


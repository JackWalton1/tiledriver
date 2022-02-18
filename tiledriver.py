# Name:         Jack Walton
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Winter 2021

import random
from typing import List, Tuple


class PuzzleState:  # do not modify

    def __init__(self, tiles: Tuple[int, ...], path: str) -> None:
        self.tiles = tiles
        self.width = int(len(tiles) ** 0.5)
        self.path = path

    def __eq__(self, other: "PuzzleState") -> bool:
        return self.tiles == other.tiles and self.path == other.path

    def __repr__(self) -> str:
        return self.path



def create_grid(tiles: Tuple[int, ...]) -> List[List[int]]:
    nums = tiles
    width = int(len(tiles) ** 0.5)
    puzzle = []
    row = []
    col = 0

    for num in nums:

        if col < width:
            row.append(num)
            col += 1
        else:
            puzzle.append(row)
            row = [num]
            col = 1

    puzzle.append(row)

    return puzzle

# state = PuzzleState((8, 7, 6, 5, 4, 3, 2, 1, 0), "J")



def get_zero_index(tiles: Tuple[int, ...]) -> int:
    index = 0
    for num in tiles:
        if num == 0:
            zero_index = index
        index += 1

    return zero_index



def find_pos_moves(puzzle: List[List[int]], previous: str) -> List[str]:
    # use is valid to find indices surrounding 0 that aren't out of range
    row = 0
    col = 0
    width = int(len(puzzle))
    for row in range(width):

        for col in range(width):

            if puzzle[row][col] == 0:
                index1, index2 = row, col

    gridmax = len(puzzle[0]) - 1
    gridmin = 0
    moves = ["K", "J", "H", "L"]

    if index1 == gridmax or previous == "J":
        moves.remove("K")

    if index1 == gridmin or previous == "K":
        moves.remove("J")

    if index2 == gridmax or previous == "L":
        moves.remove("H")

    if index2 == gridmin or previous == "H":
        moves.remove("L")

    return moves

# print(find_pos_moves(create_grid((1, 2, 3, 0, 4, 5, 6, 7, 8)), ""))
# puzzle = [[3, 2], [1, 0]]
# print(find_pos_moves(puzzle, "J"))


def make_puzzle_move(tiles: Tuple[int, ...], move: str) -> Tuple[int, ...]:

    zero_index = get_zero_index(tiles)
    width = int(len(tiles) ** .5)
    
    row_num = width - 1
    puzzle = list(tiles)

    if move == "K" and zero_index < row_num * width: # up, index 0 - 5
        # if zero_index < row_num * width: # index 0 - 5
        puzzle[zero_index], puzzle[zero_index + width] = \
            puzzle[zero_index + width], puzzle[zero_index]
        zero_index = get_zero_index(tuple(puzzle))

    if move == "J" and zero_index > row_num: # down, index 3-8
        # if zero_index > row_num: 
        puzzle[zero_index], puzzle[zero_index - width] = \
            puzzle[zero_index - width], puzzle[zero_index]
        zero_index = get_zero_index(tuple(puzzle))

    if move == "H" and (zero_index + 1) % width != 0: # left
        # if (zero_index + 1) % width != 0:
        puzzle[zero_index], puzzle[zero_index + 1] = \
            puzzle[zero_index + 1], puzzle[zero_index]
        zero_index = get_zero_index(tuple(puzzle))

    if move == "L" and (zero_index + 1) % width != 1: # right
        # if (zero_index + 1) % width != 1:
        puzzle[zero_index], puzzle[zero_index - 1] = \
            puzzle[zero_index - 1], puzzle[zero_index]
        zero_index = get_zero_index(tuple(puzzle))

    return tuple(puzzle)

# state = PuzzleState((tuple(puzzle)), move)
# state = PuzzleState((1, 2, 3, 0, 4, 5, 6, 7, 8), "J")
# print(make_puzzle_move((0, 7, 5, 8), "K"))



def make_adjacent(state: PuzzleState) -> List[PuzzleState]:
    """
    Return a list of PuzzleState objects that represent valid, non-opposing
    moves from the given PuzzleState. A move is considered valid if it moves a
    tile adjacent to the blank tile into the blank tile. A move is considered
    non-opposing if it does not undo the previous move.

    >>> state = PuzzleState((3, 2, 1, 0), "")
    >>> make_adjacent(state)
    [PuzzleState((3, 0, 1, 2), "J"), PuzzleState((3, 2, 0, 1), "L")]
    """
    puzzle = create_grid(state.tiles)
    path = state.path
    if len(path) > 0:
        previous = path[-1]
    else:
        previous = ""
    moves = find_pos_moves(puzzle, previous)
    pos_puzzles = []

    for move in moves:
        next_move = move[-1]
        pos_tiles = make_puzzle_move(state.tiles, next_move)
        ps = PuzzleState(pos_tiles, path + next_move)
        pos_puzzles.append(ps)
    
    return pos_puzzles


# state = PuzzleState((1, 2, 3, 0, 4, 5, 6, 7, 8), "K") 
# print(make_adjacent(state))
# print(state2[0].tiles)

# state = PuzzleState((3, 2, 1, 0), "")
# print(make_adjacent(state))

def find_inversions(tiles: Tuple[int, ...]) -> int:
    num_inv = 0
    tiles_list = list(tiles)
    visited = []

    for i in range(0, len(tiles) - 1):
        if tiles_list[i] > 0:
            num_not_inv = 0
            visited.append(tiles_list[i])
            for num in visited:
                if 0 < num < tiles_list[i]:
                    num_not_inv += 1
            num_inv += tiles_list[i] - num_not_inv - 1

    return num_inv

# print(find_inversions((3, 7, 1, 4, 0, 2, 6, 8, 5)))
# print(find_inversions((3, 2, 1, 0)))
# print(find_inversions((0, 2, 1, 3)))



def is_solvable(tiles: Tuple[int, ...]) -> bool:
    """
    Return a Boolean indicating whether the given tuple represents a solvable
    puzzle. Use the Merge Sort algorithm (possibly in a helper function) to
    efficiently count the number of inversions.

    >>> is_solvable((3, 2, 1, 0))
    True
    >>> is_solvable((0, 2, 1, 3))
    False
    """
    width = int(len(tiles) ** 0.5)
    puzzle = create_grid(tiles)
    inversions = find_inversions(tiles)
    if width % 2 == 1:
        if inversions % 2 == 0:
            return True

    if width % 2 == 0:
        for i in range(0, width - 1, 2):
            if 0 in puzzle[i] and inversions % 2 == 0:
                return True

        for i in range(1, width, 2):
            if 0 in puzzle[i] and inversions % 2 == 1:
                return True

    return False

# tiles = (3, 2, 1, 0)
# tiles = (3, 7, 1, 2, 0, 4, 6, 8, 5)
# tiles = (3, 7, 1, 4, 0, 2, 6, 8, 5)

# print(is_solvable(tiles))
# print(is_solvable((3, 2, 0, 1)))



def solve_puzzle(tiles: Tuple[int, ...]) -> str:
    """
    Return a string (containing characters "H", "J", "K", "L") representing the
    optimal number of moves to solve the given puzzle using Uniform Cost Search.
    A state is considered a solution if its tiles are sorted.

    >>> solve_puzzle((3, 2, 1, 0))
    "JLKHJL"
    """
    # create goal state
    goal_state = []
    for i in range(len(tiles)):
        goal_state.append(i)

    visited = []
    frontier = make_adjacent(PuzzleState(tiles, ""))
    # this was needed to fix a bug because make_adj returns a list
    # new_ps_list = []

    # i = 0
    # ps = frontier[0] 

    while frontier != []:
        ps = frontier.pop(0)
        if ps.tiles == tuple(goal_state):
            return ps.path
        if ps not in visited:
            visited.append(ps)
            new_ps_list = make_adjacent(ps)
            for new_ps in new_ps_list:
                if new_ps.tiles == tuple(goal_state):
                    return new_ps.path
                else:
                    frontier.append(new_ps)


    # finding min length path, first occurance
    # set min length to the first length
    min_len = len(visited[0].path)
    for ele in visited:  
        if len(ele.path) < min_len:  
            min_len = len(ele.path)  
            min_path = ele.path 

    return min_path

# tiles = (3, 7, 1, 4, 0, 2, 6, 8, 5)
# tiles = (1, 0, 2, 3, 4, 5, 6, 7, 8)
# repeats: KHJJLKKHJJLKKHJJLKKH


# KHJJLK * 3 + KH ???

# tiles =  (3, 6, 4, 5, 7, 2, 8, 1, 0) 

# repeats: JLKKHJJLKKHJJLKKHJJLKKH
# JLKKHJ * 3 + JLKKH ????

print(solve_puzzle(
(3, 7, 1,
 4, 0, 2, 
 6, 8, 5)
))



def main() -> None:
    random.seed(int(input("Random Seed: ")))
    tiles = list(range(int(input("Puzzle Width: ")) ** 2))  # use 2 or 3
    random.shuffle(tiles)
    print("Tiles:", "[", " ".join(str(t) for t in tiles), "]")
    if not is_solvable(tuple(tiles)):
        print("Unsolvable")
    else:
        print("Solution:", solve_puzzle(tuple(tiles)))


if __name__ == "__main__":
    main()
